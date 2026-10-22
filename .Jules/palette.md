## 2026-10-22 - Focus Ring Contrast & Fixed Headers in Dark Mode
**Learning:** In dark executive themes with fixed navigation headers, standard browser focus outlines are often low-contrast or hidden behind sticky headers. Adding a high-contrast `:focus-visible` ring using brand accents (`var(--accent-cyan)`) and a high z-index skip-link ensures seamless keyboard accessibility.
**Action:** When working on dark-themed single page landing sites, always implement an accessible skip-link (`z-index: 9999`) and explicit `:focus-visible` ring styles mapped to primary design tokens.
