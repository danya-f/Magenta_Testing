from data.locators import SignInPageLocators
from pages.signin_page import SignInPage
from data.urls import ACCOUNT_PAGE_URL


class TestSignIn:

    def test_good_email_password(self, driver, good_email, good_password):
        page = SignInPage(driver)
        page.login_with_good_email_password(good_email , good_password)
        assert page.current_url() == ACCOUNT_PAGE_URL , "Не удалось залогиниться в существующий аккаунт , функция автологин"

    def test_bad_password(self, driver, good_email, fake_password):
        page = SignInPage(driver)
        page.login_with_incorrect_password(good_email,fake_password)
        assert page.current_url() != ACCOUNT_PAGE_URL, "удалось залогиниться с неправильным паролем"
        assert page.error_signin_msg().text == SignInPageLocators.TEXT_ERROR_SIGNIN_MSG, "неправильное сообщение об ошибке при попытке логина с неправильным паролем"

    def test_bad_email_password(self, driver, fake_email, fake_password):
        page = SignInPage(driver)
        page.login_with_fake_email_password(fake_email , fake_password)
        assert page.current_url() != ACCOUNT_PAGE_URL, "удалось залогиниться в несуществующий аккаунт"
        assert page.error_signin_msg().text == SignInPageLocators.TEXT_ERROR_SIGNIN_MSG, "неправильное сообщение об ошибке при попытке логина с фейковыми данными, функция автологин"

    # def test_with_good_email_password(self, driver, good_email, good_password):
    #     page = SignInPage(driver)
    #     page.open()
    #     page.email_field().send_keys(good_email)
    #     page.password_field().send_keys(good_password)
    #     page.signin_button().click()
    #     assert page.current_url() == ACCOUNT_PAGE_URL, "Не удалось залогиниться в существующий аккаунт"
    #
    # def test_with_bad_email_password(self, driver, fake_email, fake_password):
    #     page = SignInPage(driver)
    #     page.open()
    #     page.email_field().send_keys(fake_email)
    #     page.password_field().send_keys(fake_password)
    #     page.signin_button().click()
    #     assert page.current_url() != ACCOUNT_PAGE_URL, "удалось залогиниться в несуществующий аккаунт"
    #     assert page.error_signin_msg().text == SignInPageLocators.TEXT_ERROR_SIGNIN_MSG, "неправильное сообщение об ошибке при попытке логина с фейковыми данными"
