import pytest

from models.page_objects.welcome_page import WelcomePage
from models.page_objects.app_page import AppPage
from models.page_objects.card_1_form import Card1Form
from models.page_objects.card_2_form import Card2Form
from models.page_objects.cookies_banner import CookiesBanner
from models.page_objects.help_form import HelpForm

from utils.browser_utils import BrowserUtils

@pytest.fixture(scope="function", autouse=True)
def before_each(welcome_page: WelcomePage, app_page: AppPage, pytestconfig: pytest.Config, browser_utils: BrowserUtils):
    base_url = pytestconfig.getini('base_url')
    browser_utils.navigate_to(base_url)
    welcome_page.is_opened()
    welcome_page.go_to_card_page()
    app_page.is_opened("1")

def test_case_1(app_page: AppPage, card_1_form: Card1Form, card_2_form: Card2Form):
    card_1_form.login()
    app_page.is_opened("2")
    card_2_form.unselect_all_interests()
    card_2_form.select_random_interests(3)
    card_2_form.go_to_card_3()
    #app_page.is_opened("3")

def test_case_2(help_form: HelpForm):
    help_form.hide()
    help_form.is_hidden(True) 

def test_case_3(cookies_banner: CookiesBanner):
    cookies_banner.accept_cookies()
    cookies_banner.is_displayed(False)

def test_case_4(app_page: AppPage):
    app_page.timer_starts_from_0()