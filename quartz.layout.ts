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
    const order = ["leerpaden", "themafiches", "concepten"]
    const ai = order.indexOf(a.slugSegment)
    const bi = order.indexOf(b.slugSegment)
    if (ai !== -1 && bi !== -1) return ai - bi
    if (ai !== -1) return -1
    if (bi !== -1) return 1

    // ITAA-LEX volgorde voor bronnen/wetteksten
    const aSlug: string = a.slug ?? ""
    const bSlug: string = b.slug ?? ""
    if (aSlug.includes("bronnen/wetteksten") && bSlug.includes("bronnen/wetteksten")) {
      const itaaLexOrder = [
        "i-voorafgaande-beslissingen",
        "ii-wib92",
        "ii-kb-wib92",
        "iii-wigb",
        "iva-vcf",
        "ivb-brussel-fiscale-procedure",
        "ivc-waals-gewestelijke-belastingen",
        "v-wdrt",
        "via-wbtw",
        "vii-wetboek-invordering",
        "viii-registratierechten",
        "viii-registratierechten-federaal",
        "viii-registratierechten-brussel",
        "viii-registratierechten-waals",
        "ix-successierechten",
        "ix-successierechten-brussel",
        "ix-successierechten-waals",
        "ix-successierechten-federaal",
        "x-eu-belastingen",
        "xi-bw-2019",
        "xi-oud-bw",
        "xii-strafwetboek",
        "xiii-wer",
        "xiii-kb-wer-boekhouding",
        "xiv-betalingsachterstand",
        "xv-wvv",
        "xv-kb-wvv",
        "xvi-arbeidsovereenkomsten",
        "xvii-antiwitwaswet",
        "xviii-klokkenluiders",
        "xix-avg",
        "xx-eu-beroepskwalificaties",
        "xxi-wet-itaa",
        "eu-richtlijn-2013-34",
      ]
      const aIdx = itaaLexOrder.indexOf((a.slugSegment as string).toLowerCase())
      const bIdx = itaaLexOrder.indexOf((b.slugSegment as string).toLowerCase())
      if (aIdx !== -1 && bIdx !== -1) return aIdx - bIdx
      if (aIdx !== -1) return -1
      if (bIdx !== -1) return 1
    }

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
  afterBody: [Component.CollapsibleSteps()],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/stivni/certificaid",
    },
  }),
}

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ArticleTitle(),
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
