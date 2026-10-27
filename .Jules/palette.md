## 2026-10-27 - Focus Visible Indicators and Skip Links for Dark Themes
**Learning:** Dark executive themes (#08090C backgrounds) render default browser focus rings almost invisible or inconsistent, hindering keyboard navigation accessibility.
**Action:** Always include a `.skip-link` visually hidden until focused, and define high-contrast `:focus-visible` outline rings using the theme accent color (`var(--accent-cyan)`).
