from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")


class SiteChecks(unittest.TestCase):
    def test_mobile_navigation_is_present(self):
        self.assertIn('id="mobile-menu-toggle"', HTML)
        self.assertIn('id="mobile-menu"', HTML)
        self.assertIn('aria-controls="mobile-menu"', HTML)

    def test_placeholder_links_are_removed(self):
        self.assertNotIn('href="#"', HTML)

    def test_frontend_password_prompt_is_removed(self):
        self.assertNotIn("correctPassword", HTML)
        self.assertNotIn("prompt(", HTML)
        self.assertNotIn("mimo", HTML)

    def test_contact_form_uses_mail_client_instead_of_fake_success(self):
        self.assertIn("mailto:wisdomzo@dev.com", HTML)
        self.assertNotIn("发送成功", HTML)
        self.assertNotIn("setTimeout", HTML)

    def test_half_finished_theme_toggle_is_removed(self):
        self.assertNotIn('id="theme-toggle"', HTML)
        self.assertNotIn("主题切换", HTML)

if __name__ == "__main__":
    unittest.main()
