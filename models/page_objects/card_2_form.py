from playwright.sync_api import Page

from models.page_objects.base_page import BasePage
from models.locators.card_2_form_locators import Card2FormLocators

from utils.random_utils import RandomUtils

class Card2Form(BasePage):
    def __init__(self, page: Page):        
        super().__init__(page)
        self.upload_avatar_link = page.locator(Card2FormLocators.UPLOAD_AVATAR_LINK)
        self.interests = page.locator(Card2FormLocators.INTERESTS)
        self.unselect_all_checkbox = page.locator(Card2FormLocators.UNSELECT_ALL_CHECKBOX)
        self.next_button = page.get_by_text(Card2FormLocators.NEXT_BUTTON)
    
    def unselect_all_interests(self):
        self.unselect_all_checkbox.click()

    def select_random_interests(self, number: int):
        indexes = []
        i = 0
        while i < number: 
            index = RandomUtils.get_random_int(self.interests.count() - 1)
            if index not in indexes:
                indexes.append(index)
                i += 1

        for i in indexes:
            self.interests.nth(i).click()

    def go_to_card_3(self):
        self.next_button.click()

    def upload_avatar(self, photo_path: str):
        self.upload_avatar_link.set_input_files(photo_path)
