from playwright.sync_api import Page, expect

from models.page_objects.base_page import BasePage
from models.locators.cookies_banner_locators import CookiesBannerLocators

class CookiesBanner(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cookies_banner = page.locator(CookiesBannerLocators.COOKIES_BANNER)
        self.accept_cookies_button = page.locator(CookiesBannerLocators.ACCEPT_COOKIES_BUTTON)
    
    def accept_cookies(self):
        self.accept_cookies_button.click()

    def is_displayed(self, isDisplayed: bool):
        if(isDisplayed):
            expect(self.cookies_banner).to_be_visible()
        else:
            expect(self.cookies_banner).not_to_be_visible()