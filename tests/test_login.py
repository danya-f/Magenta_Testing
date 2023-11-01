from pages.main_page import MainPage
from data.urls import MAIN_PAGE_URL



class Test_SignIn:

    def test_signin_good_email_pass(self , driver):
        page = MainPage(driver ,MAIN_PAGE_URL )
        page.open()
        page.signin_click().click()

