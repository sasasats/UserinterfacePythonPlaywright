from playwright.sync_api import Page, expect

from models.page_objects.base_page import BasePage
from models.locators.welcome_page_locators import WelcomePageLocators

class WelcomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.start_link = page.locator(WelcomePageLocators.START_LINK)
        self.logo = page.locator(WelcomePageLocators.LOGO)
    
    def navigate(self):
        self.page.goto('https://userinyerface.com/')
    
    def go_to_card_page(self):
        self.start_link.click()
    
    def is_opened(self):
        expect(self.logo).to_be_visible()