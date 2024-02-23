from playwright.sync_api import Page

from models.page_objects.base_page import BasePage

class BrowserUtils(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to(self, url: str):
        self.page.goto(url)