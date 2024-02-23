from playwright.sync_api import Page, expect

from models.page_objects.base_page import BasePage
from models.locators.help_form_locators import HelpFormLocators

class HelpForm(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.help_form = page.locator(HelpFormLocators.HELP_FORM)
        self.send_to_bottom_button = page.locator(HelpFormLocators.HIDE_HELP_FORM_BUTTON)
    
    def hide(self):
        self.send_to_bottom_button.click()

    def is_hidden(self, isDisplayed: bool):
        if(isDisplayed):
            expect(self.help_form).to_have_attribute('class', 'help-form is-hidden')
        else:
            expect(self.help_form).not_to_have_attribute('class', 'help-form is-hidden')