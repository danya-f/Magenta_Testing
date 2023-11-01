from pages.any_page import AnyPage
from pages.signin_page import SignInPage
from data.urls import SIGNIN_PAGE_URL, ACCOUNT_PAGE, ERROR_SIGNIN_MSG


class Test_SignIn:

    def test_with_good_email_password(self, driver, good_email, good_password):
        page = SignInPage(driver, SIGNIN_PAGE_URL)
        page.open()
        page.email_field().send_keys(good_email)
        page.password_field().send_keys(good_password)
        page.signin_button().click()
        assert page.current_url() == ACCOUNT_PAGE, "Не удалось залогиниться в существующий аккаунт"

    def test_with_bad_email_password(self, driver, fake_email, fake_password):
        page = SignInPage(driver, SIGNIN_PAGE_URL)
        page.open()
        page.email_field().send_keys(fake_email)
        page.password_field().send_keys(fake_password)
        page.signin_button().click()
        assert page.current_url() != ACCOUNT_PAGE, "удалось залогиниться в несуществующий аккаунт"
        assert page.error_signin_msg().text == ERROR_SIGNIN_MSG, "неправильное сообщение об ошибке при попытке логина с фейковыми данными"

    def test_with_bad_password(self, driver, good_email, fake_password):
        page = SignInPage(driver, SIGNIN_PAGE_URL)
        page.open()
        page.email_field().send_keys(good_email)
        page.password_field().send_keys(fake_password)
        page.signin_button().click()
        assert page.current_url() != ACCOUNT_PAGE, "удалось залогиниться с неправильным паролем"
        assert page.error_signin_msg().text == ERROR_SIGNIN_MSG, "неправильное сообщение об ошибке при попытке логина с неправильным паролем"
