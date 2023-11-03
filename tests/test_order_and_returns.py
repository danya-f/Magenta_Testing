from data.locators import OrdersAndReturnsPageLocators
from pages.orders_and_returns_page import OrdersAndReturnsPage
#временно
from time import sleep


class TestFieldsNotFilled:
    def test_order_id_field_not_filled(self,driver,fake_email,fake_lastname):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.email_field().send_keys(fake_email)
        page.billing_lastname_field().send_keys(fake_lastname)
        page.continue_button().click()
        assert page.error_order_id_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD , "Поле order_id не заполнено , а ошибка не показана"

    def test_lastname_field_not_filled(self,driver,fake_email,fake_password,fake_order_id):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.order_id_field().send_keys(fake_order_id)
        page.email_field().send_keys(fake_email)
        page.continue_button().click()
        assert page.error_billing_lastname_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD , "Поле billing lastname не заполнено , а ошибка не показана"

    def test_email_field_not_filled(self,driver,fake_lastname,fake_order_id):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.order_id_field().send_keys(fake_order_id)
        page.billing_lastname_field().send_keys(fake_lastname)
        page.continue_button().click()
        assert page.error_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD , "Поле email не заполнено , а ошибка не показана"

    def test_zip_field_not_filled(self,driver,fake_lastname,fake_order_id,fake_zip_code):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.order_id_field().send_keys(fake_order_id)
        page.billing_lastname_field().send_keys(fake_lastname)
        page.select_find_order_by_zip_code_dropdown()
        page.continue_button().click()
        assert page.error_billing_zip_code_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD , "Поле zipcode не заполнено , а ошибка не показана"

    def test_email_filled_incorrect_email_type(self,driver,fake_lastname,fake_order_id,incorrect_type_email):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.order_id_field().send_keys(fake_order_id)
        page.email_field().send_keys(incorrect_type_email)
        page.billing_lastname_field().send_keys(fake_lastname)
        page.continue_button().click()
        assert page.error_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE


class TestFindOrderBySwitch:

    def test_switch_to_zip(self,driver):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.select_find_order_by_zip_code_dropdown()
        assert page.label_billing_zip_code().text == OrdersAndReturnsPageLocators.TEXT_LABEL_ZIP_FIELD ,'не произошло переключение поиска заказа с Email на ZIP'

    def test_switch_to_email(self, driver):
        page = OrdersAndReturnsPage(driver)
        page.open()
        page.select_find_order_by_zip_code_dropdown()
        assert page.label_billing_zip_code().text == OrdersAndReturnsPageLocators.TEXT_LABEL_ZIP_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'
        page.select_find_order_by_email_dropdown()
        assert page.label_email().text == OrdersAndReturnsPageLocators.TEXT_LABEL_EMAIL_FIELD , 'не произошло переключение поиска заказа с ZIP на Email'

