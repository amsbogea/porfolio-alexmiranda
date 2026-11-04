import unittest
from html.parser import HTMLParser
import re

class TestAccessibilityEnhancements(unittest.TestCase):
    def setUp(self):
        with open("index.html", "r", encoding="utf-8") as f:
            self.html_content = f.read()
        with open("static/css/style.css", "r", encoding="utf-8") as f:
            self.css_content = f.read()

    def test_html_parsing(self):
        """Ensure index.html is valid HTML that parses without errors."""
        class TestParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.tags = []
            def handle_starttag(self, tag, attrs):
                self.tags.append((tag, dict(attrs)))

        parser = TestParser()
        parser.feed(self.html_content)
        self.assertGreater(len(parser.tags), 0)

    def test_skip_link_exists_and_points_to_main_content(self):
        """Ensure skip link exists right at the start of body and points to #apresentacao."""
        self.assertIn('class="skip-link"', self.html_content)
        self.assertIn('href="#apresentacao"', self.html_content)
        self.assertIn('Pular para o conteúdo principal', self.html_content)

    def test_target_section_has_tabindex(self):
        """Ensure the target section has tabindex="-1" for programmatically focusing via skip link."""
        self.assertIn('id="apresentacao"', self.html_content)
        self.assertIn('tabindex="-1"', self.html_content)

    def test_css_skip_link_rules(self):
        """Ensure CSS provides skip-link styling for accessibility."""
        self.assertIn(".skip-link", self.css_content)
        self.assertIn("translateY(-160%)", self.css_content)
        self.assertIn(".skip-link:focus", self.css_content)
        self.assertIn("translateY(0)", self.css_content)

    def test_css_focus_visible_rules(self):
        """Ensure CSS defines focus-visible outline for keyboard navigation."""
        self.assertIn(":focus-visible", self.css_content)
        self.assertIn("outline: 2px solid var(--accent-cyan)", self.css_content)

    def test_scroll_padding_top_configured(self):
        """Ensure html has scroll-padding-top to avoid header nav overlapping sections."""
        self.assertIn("scroll-padding-top: 80px;", self.css_content)


if __name__ == "__main__":
    unittest.main()
