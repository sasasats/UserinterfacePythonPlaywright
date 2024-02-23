from playwright.sync_api import Page

from models.page_objects.base_page import BasePage
from models.locators.card_1_form_locators import Card1FormLocators

from utils.element_utils import ElementUtils

class Card1Form(BasePage):
    def __init__(self, page: Page):        
        super().__init__(page)
        self.password_field = page.locator(Card1FormLocators.PASSWORD_FIELD)
        self.email_field = page.locator(Card1FormLocators.EMAIL_FIELD)
        self.domain_field = page.locator(Card1FormLocators.DOMAIN_FIELD)
        self.domain_dropdown_opener = page.locator(Card1FormLocators.DOMAIN_DROPDOWN_OPENER)
        self.domains = page.locator(Card1FormLocators.DOMAINS)
        self.accept_terms_checkbox = page.locator(Card1FormLocators.ACCEPT_TERMS_CHECKBOX)
        self.next_button = page.locator(Card1FormLocators.NEXT_BUTTON)

    def login(self):
        self.password_field.clear()
        self.password_field.fill("AndreySats1999")

        self.email_field.clear()
        self.email_field.fill("a.sats")

        self.domain_dropdown_opener.click()
        ElementUtils.get_random_element(self.domains).click()

        self.domain_field.clear()
        self.domain_field.fill("a1qa")

        self.accept_terms_checkbox.click()
        self.next_button.click()