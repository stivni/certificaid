import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

const explorerOpts = {
  mapFn: (node: any) => {
    // Use explorer_title frontmatter field when available (programmaonderdelen)
    if (node.file?.frontmatter?.explorer_title) {
      node.displayName = node.file.frontmatter.explorer_title
      return node
    }
    return node
  },
  sortFn: (a: any, b: any) => {
    const order = ["programmaonderdelen", "competenties", "materie", "bronnen"]
    const ai = order.indexOf(a.slugSegment)
    const bi = order.indexOf(b.slugSegment)
    if (ai !== -1 && bi !== -1) return ai - bi
    if (ai !== -1) return -1
    if (bi !== -1) return 1
    return a.displayName.localeCompare(b.displayName, "nl")
  },
  filterFn: (node: any) => {
    if (node.slugSegment === "tags") return false
    if (node.data?.tags?.includes("verborgen")) return false
    return true
  },
}

const controls = Component.Flex({
  components: [
    { Component: Component.Search(), grow: true },
    { Component: Component.Darkmode() },
    { Component: Component.ReaderMode() },
  ],
  direction: "row",
  gap: "0.5rem",
})

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/stivni/certificaid",
    },
  }),
}

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    // Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    controls,
    Component.DesktopOnly(Component.Explorer(explorerOpts)),
  ],
  right: [
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [
    Component.ArticleTitle(),
    Component.ContentMeta(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    controls,
    Component.DesktopOnly(Component.Explorer(explorerOpts)),
  ],
  right: [],
}
