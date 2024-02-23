from playwright.sync_api import Page, expect

from models.page_objects.base_page import BasePage
from models.locators.app_page_locators import AppPageLocators

from utils.element_utils import ElementUtils



class AppPage(BasePage):
    def __init__(self, page: Page):        
        super().__init__(page)
        self.timer = page.locator(AppPageLocators.TIMER)
        self.page_indicator = page.locator(AppPageLocators.PAGE_INDICATOR)
    
    def is_opened(self, card_number: str):
        expect(self.page_indicator).to_have_text(f"{card_number} / 4")

    def timer_starts_from_0(self):
        expect(self.timer).to_have_text('00:00:00')