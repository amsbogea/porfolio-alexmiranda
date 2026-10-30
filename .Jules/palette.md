## 2026-10-30 - Focus Visible Navigation Ring
**Learning:** Custom button and anchor styles without explicit `:focus-visible` CSS rules prevent keyboard-only users from seeing active focus position in dark themes.
**Action:** Always declare standard `:focus-visible` focus rings tied to high-contrast cyan accent colors (`var(--accent-cyan)` and `var(--accent-glow)`) on global reset layers.
