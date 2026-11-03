# Palette's UX Journal

## 2026-11-03 - High-Contrast Dark Mode Focus Indicators & Skip Links
**Learning:** In executive dark-mode interfaces dominated by dark surfaces (`--bg-base: #08090C`, `--bg-surface: #0E1117`), standard browser focus outlines are often low-contrast or visually lost against dark backgrounds. Using high-contrast cyan (`--accent-cyan`) outlines with offset alongside a fixed-positioned skip-to-content navigation pattern ensures seamless screen reader and keyboard accessibility without disturbing visual aesthetics for pointer users.
**Action:** Always provide dedicated `:focus-visible` styling paired with the primary accent color and a `#conteudo-principal` skip link for fixed-header portfolio layouts.
