# Palette's Journal - Critical UX Learnings

## 2025-05-18 - Fixed Navbar Scroll Offset with Skip-to-Content Pattern
**Learning:** Fixed navigation headers (`position: fixed; height: 70px`) obscure content targeted by skip links or in-page anchor navigations when jumping to landmark containers. In addition to a semantic skip-link, applying `scroll-padding-top` on `html` and `tabindex="-1"` on `<main>` ensures focus shifts correctly to the main content landmark without getting hidden beneath the header.
**Action:** Always pair in-page skip links and anchor links with CSS `html { scroll-padding-top: [navbar-height]; }` and set `tabindex="-1"` on the destination landmark with `:focus { outline: none; }` to maintain smooth, accessible keyboard navigation without visual glitches.
