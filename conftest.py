import pytest
from playwright.sync_api import Page

from models.page_objects.welcome_page import WelcomePage
from models.page_objects.app_page import AppPage
from models.page_objects.card_1_form import Card1Form
from models.page_objects.card_2_form import Card2Form
from models.page_objects.cookies_banner import CookiesBanner
from models.page_objects.help_form import HelpForm

from utils.browser_utils import BrowserUtils

@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': 1920,
            'height': 1080,
        },
    }

@pytest.fixture()
def browser_utils(page: Page):
    return BrowserUtils(page)

@pytest.fixture()
def welcome_page(page: Page):
    return WelcomePage(page)

@pytest.fixture()
def app_page(page: Page):
    return AppPage(page)

@pytest.fixture()
def card_1_form(page: Page):
    return Card1Form(page)

@pytest.fixture()
def card_2_form(page: Page):
    return Card2Form(page)

@pytest.fixture()
def cookies_banner(page: Page):
    return CookiesBanner(page)

@pytest.fixture()
def help_form(page: Page):
    return HelpForm(page)