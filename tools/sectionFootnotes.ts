import { QuartzTransformerPlugin } from "../quartz/plugins/types"

/**
 * Injects CSS to style inline citation links (wikilinks to itaa-lex or wetteksten)
 * as small, discrete superscript-like elements that don't interrupt reading flow.
 */
export const SectionFootnotes: QuartzTransformerPlugin = () => {
  return {
    name: "SectionFootnotes",
    externalResources() {
      return {
        css: [
          {
            inline: true,
            content: `
/* Inline citation links — smaller and gray so they don't compete with body text */
a.internal[href*="itaa-lex"],
a.internal[href*="wetteksten"] {
  font-size: 0.8em;
  color: var(--gray);
  text-decoration: none;
  font-style: normal;
}
a.internal[href*="itaa-lex"]:hover,
a.internal[href*="wetteksten"]:hover {
  color: var(--secondary);
  text-decoration: underline;
}
`,
          },
        ],
      }
    },
  }
}
