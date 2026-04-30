import { QuartzTransformerPlugin } from "../quartz/plugins/types"
import { visit } from "unist-util-visit"
import type { Root, Element, RootContent } from "hast"

/**
 * Moves footnote definitions from the bottom of the page to directly after the
 * section (h1/h2/h3) where the footnote reference appears.
 *
 * Works by post-processing the HTML AST after remark-gfm has rendered footnotes.
 */
export const SectionFootnotes: QuartzTransformerPlugin = () => {
  return {
    name: "SectionFootnotes",
    htmlPlugins(_ctx) {
      return [
        () => (tree: Root) => {
          // Step 1: find and extract the global footnotes section
          const footnoteMap = new Map<string, Element>()
          let globalFootnotesIdx = -1

          for (let i = 0; i < tree.children.length; i++) {
            const node = tree.children[i]
            if (
              node.type === "element" &&
              node.tagName === "section" &&
              "dataFootnotes" in (node.properties ?? {})
            ) {
              globalFootnotesIdx = i
              const ol = node.children.find(
                (c): c is Element => c.type === "element" && (c as Element).tagName === "ol",
              )
              if (ol) {
                for (const child of ol.children) {
                  if (
                    child.type === "element" &&
                    child.tagName === "li" &&
                    child.properties?.id
                  ) {
                    footnoteMap.set(child.properties.id as string, child)
                  }
                }
              }
              break
            }
          }

          if (footnoteMap.size === 0) return

          // Remove the global footnotes section; indices below are based on the
          // resulting (shorter) children array.
          tree.children.splice(globalFootnotesIdx, 1)

          // Step 2: locate section boundaries (headings h1–h3)
          const headingTags = new Set(["h1", "h2", "h3"])
          const headingIndices: number[] = []
          for (let i = 0; i < tree.children.length; i++) {
            const node = tree.children[i]
            if (node.type === "element" && headingTags.has(node.tagName)) {
              headingIndices.push(i)
            }
          }

          // Build section spans [start, end] (inclusive)
          const sections: Array<{ start: number; end: number }> = []
          if (headingIndices.length === 0) {
            sections.push({ start: 0, end: tree.children.length - 1 })
          } else {
            if (headingIndices[0] > 0) {
              sections.push({ start: 0, end: headingIndices[0] - 1 })
            }
            for (let h = 0; h < headingIndices.length; h++) {
              sections.push({
                start: headingIndices[h],
                end:
                  h + 1 < headingIndices.length
                    ? headingIndices[h + 1] - 1
                    : tree.children.length - 1,
              })
            }
          }

          // Step 3: for each section find referenced footnote IDs
          const insertions: Array<{ afterIndex: number; ids: string[] }> = []

          for (const { start, end } of sections) {
            const referencedIds: string[] = []
            const fakeRoot: Root = {
              type: "root",
              children: tree.children.slice(start, end + 1) as RootContent[],
            }

            visit(fakeRoot, "element", (node: Element) => {
              if (
                node.tagName === "a" &&
                typeof node.properties?.href === "string" &&
                // "#user-content-fn-X" → footnote reference
                // "#user-content-fnref-X" → back-reference (already removed)
                node.properties.href.startsWith("#user-content-fn-") &&
                !node.properties.href.startsWith("#user-content-fnref-")
              ) {
                const id = node.properties.href.slice(1) // strip leading #
                if (!referencedIds.includes(id)) {
                  referencedIds.push(id)
                }
              }
            })

            if (referencedIds.length > 0) {
              insertions.push({ afterIndex: end, ids: referencedIds })
            }
          }

          // Step 4: insert mini-sections back-to-front to keep earlier indices stable
          for (let i = insertions.length - 1; i >= 0; i--) {
            const { afterIndex, ids } = insertions[i]
            const liElements = ids
              .map((id) => footnoteMap.get(id))
              .filter((el): el is Element => el !== undefined)

            if (liElements.length === 0) continue

            const miniSection: Element = {
              type: "element",
              tagName: "section",
              properties: { className: ["section-footnotes"] },
              children: [
                {
                  type: "element",
                  tagName: "ol",
                  properties: {},
                  children: liElements,
                },
              ],
            }

            tree.children.splice(afterIndex + 1, 0, miniSection)
          }
        },
      ]
    },
    externalResources() {
      return {
        css: [
          {
            inline: true,
            content: `
.section-footnotes {
  font-size: 0.85em;
  color: var(--gray);
  border-top: 1px solid var(--lightgray);
  margin-top: 1.5rem;
  padding-top: 0.75rem;
}
.section-footnotes ol {
  margin: 0;
  padding-left: 1.5em;
}
.section-footnotes li {
  margin-bottom: 0.25rem;
}
.section-footnotes a.data-footnote-backref {
  margin-left: 0.25em;
  font-style: normal;
}
/* Hide the original (now empty) global footnotes block */
section.footnotes {
  display: none;
}
`,
          },
        ],
      }
    },
  }
}
