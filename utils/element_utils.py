from playwright.sync_api import Locator
import random

class ElementUtils:
    
    @staticmethod
    def get_random_element(locator: Locator):
        return locator.nth(random.randint(0, locator.count() - 1))