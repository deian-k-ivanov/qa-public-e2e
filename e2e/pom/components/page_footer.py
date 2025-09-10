from playwright.sync_api import Page, expect


class PageFooter:
    def __init__(self, *, page: Page):
        self.page = page
        self.footer = page.get_by_test_id("footer")
        self.twitter_link = self.footer.get_by_test_id("social-twitter")
        self.facebook_link = self.footer.get_by_test_id("social-facebook")
        self.linkedin_link = self.footer.get_by_test_id("social-linkedin")
        self.footer_copyright = self.footer.get_by_test_id("footer-copy")

    def assert_all_footer_elements_are_present(self) -> None:
        expect(self.twitter_link).to_be_visible()
        expect(self.facebook_link).to_be_visible()
        expect(self.linkedin_link).to_be_visible()
        expect(self.footer_copyright).to_be_visible()
