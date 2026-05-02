// @ts-ignore
import collapsibleStepsScript from "./scripts/collapsible-steps.inline"
import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

// Renders nothing — exists only to register the collapsible-steps script.
function CollapsibleSteps(_props: QuartzComponentProps) {
  return null
}

CollapsibleSteps.afterDOMLoaded = collapsibleStepsScript

export default (() => CollapsibleSteps) satisfies QuartzComponentConstructor
