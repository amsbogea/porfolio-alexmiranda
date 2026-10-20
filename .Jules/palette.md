## 2025-05-18 - Navigation Focus & External Link Accessibility
**Learning:** External links with `target="_blank"` without explicit `aria-label` context do not announce to screen readers that a new browser window/tab will open. Additionally, missing `:focus-visible` styles lead to invisible keyboard focus on navigation links.
**Action:** Always add `rel="noopener noreferrer"` and `aria-label="... (abre em nova janela)"` to `target="_blank"` links, and provide high-contrast `:focus-visible` outlines for interactive navigation elements.
