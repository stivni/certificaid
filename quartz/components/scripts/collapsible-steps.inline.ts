function handleStepClick(e: Event) {
  const h3 = e.currentTarget as HTMLElement
  // Don't toggle when clicking the anchor link (the # permalink) inside h3
  const target = e.target as HTMLElement
  if (target !== h3 && target.closest("a")) return

  const wrapper = h3.parentElement as HTMLElement
  const content = wrapper.querySelector(".step-content") as HTMLElement | null
  if (!content) return

  const collapsed = wrapper.classList.toggle("is-collapsed")
  content.style.gridTemplateRows = collapsed ? "0fr" : "1fr"
  h3.setAttribute("aria-expanded", String(!collapsed))
}

function handleStepKeydown(e: Event) {
  const ke = e as KeyboardEvent
  if (ke.key !== "Enter" && ke.key !== " ") return
  ke.preventDefault()
  handleStepClick(e)
}

function setupCollapsibleSteps() {
  // Only on pages tagged 'competentie'
  if (!document.querySelector('a.tag-link[href*="tags/competentie"]')) return

  const article = document.querySelector("article")
  if (!article) return

  // Only process unhandled h3s
  const h3s = Array.from(article.querySelectorAll<HTMLElement>("h3")).filter(
    (h3) => !h3.closest(".step-wrapper"),
  )

  for (const h3 of h3s) {
    // Collect sibling elements until the next heading
    const siblings: Element[] = []
    let next = h3.nextElementSibling
    while (next && !["H1", "H2", "H3"].includes(next.tagName)) {
      siblings.push(next)
      next = next.nextElementSibling
    }

    // Wrapper (collapsed by default)
    const wrapper = document.createElement("div")
    wrapper.className = "step-wrapper is-collapsed"

    // Outer content div acts as CSS grid (for smooth height transition)
    const contentOuter = document.createElement("div")
    contentOuter.className = "step-content"
    contentOuter.style.gridTemplateRows = "0fr"

    // Inner div — the single grid child; overflow hidden to allow collapse
    const contentInner = document.createElement("div")
    contentInner.className = "step-content-inner"
    contentOuter.appendChild(contentInner)

    // Restructure DOM: wrapper contains h3 + contentOuter
    h3.parentNode!.insertBefore(wrapper, h3)
    wrapper.appendChild(h3)
    for (const s of siblings) contentInner.appendChild(s)
    wrapper.appendChild(contentOuter)

    // Add chevron indicator
    const chevron = document.createElement("span")
    chevron.className = "step-chevron"
    chevron.setAttribute("aria-hidden", "true")
    h3.appendChild(chevron)

    // Accessibility
    h3.setAttribute("role", "button")
    h3.setAttribute("tabindex", "0")
    h3.setAttribute("aria-expanded", "false")

    h3.addEventListener("click", handleStepClick)
    h3.addEventListener("keydown", handleStepKeydown)
    window.addCleanup(() => {
      h3.removeEventListener("click", handleStepClick)
      h3.removeEventListener("keydown", handleStepKeydown)
    })
  }
}

document.addEventListener("nav", setupCollapsibleSteps)
