from pages.my_accoun_page import MyAccountPage
from pages.signin_page import SignInPage
from data.urls import STORED_PAYMENT_METHODS_USR, MY_ACCOUNT_URL, MY_DOWNLOADABLE_PRODUCTS_URL, MY_PRODUCT_REVIEW_URL, \
    MY_ORDERS_URL, MY_WISH_LIST_URL, ADDRESS_BOOK_URL, ACCOUNT_INFORMATION_URL


# временно
# from time import sleep


class TestMyAccountSwitchingButtons:

    def test_my_account_button(self, driver, good_password, good_email):
        page = SignInPage(driver)
        my_account_page = page.login_with_good_email_password(good_email, good_password)
        my_account_page.my_orders_button().click()
        my_account_page.my_account_button().click()
        assert my_account_page.current_url() == MY_ACCOUNT_URL, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ МОЙ АККАУНТ"

    def test_my_orders_button(self, driver, good_password, good_email):
        page = SignInPage(driver)
        my_account_page = page.login_with_good_email_password(good_email, good_password)
        my_account_page.my_orders_button().click()
        assert my_account_page.current_url() == MY_ORDERS_URL, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ ЗАКАЗОВ"

    def test_my_downloadable_products_button(self, driver, good_password, good_email):
        page = SignInPage(driver)
        my_account_page = page.login_with_good_email_password(good_email, good_password)
        my_account_page.my_downloadable_products_button().click()
        assert my_account_page.current_url() == MY_DOWNLOADABLE_PRODUCTS_URL, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ DOWNLOADABLE PRODUCTS"

    def test_my_wish_list_button(self, driver, good_password, good_email):
        page = SignInPage(driver)
        my_account_page = page.login_with_good_email_password(good_email, good_password)
        my_account_page.my_wish_list_button().click()
        assert my_account_page.current_url() == MY_WISH_LIST_URL, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ WISH LIST"

    def test_address_book_button(self, driver, good_password, good_email):
        page = SignInPage(driver)
        my_account_page = page.login_with_good_email_password(good_email, good_password)
        my_account_page.address_book_button().click()
        assert my_account_page.current_url() == ADDRESS_BOOK_URL, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ ADRESS BOOK"

    def test_account_information_button(self, driver, good_password, good_email):
        page = SignInPage(driver)
        my_account_page = page.login_with_good_email_password(good_email, good_password)
        my_account_page.account_information_button().click()
        assert my_account_page.current_url() == ACCOUNT_INFORMATION_URL, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ ACCOUNT INFORMATION"

    def test_stored_payment_methods_button(self, driver, good_password, good_email):
        page = SignInPage(driver)
        my_account_page = page.login_with_good_email_password(good_email, good_password)
        my_account_page.stored_payment_methods_button().click()
        assert my_account_page.current_url() == STORED_PAYMENT_METHODS_USR, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ PAYMENT METHODS"

    def test_my_product_review_button(self, driver, good_password, good_email):
        page = SignInPage(driver)
        my_account_page = page.login_with_good_email_password(good_email, good_password)
        my_account_page.my_product_reviews_button().click()
        assert my_account_page.current_url() == MY_PRODUCT_REVIEW_URL, "НЕ УДАЛОСЬ ПЕРЕЙТИ НА СТРАНИЦУ MY PRODUCT REVIEW"

# class TestSwitchButtonsName:
#
#     def test_my_account_button(self,driver,good_password,good_email):
#         page = SignInPage(driver)
#         my_account_page = page.login_with_good_email_password(good_email, good_password)
#         assert my_account_page.my_account_button().text == "My "