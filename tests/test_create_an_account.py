from data.locators import CreateAnAccountPageLocators
from pages.create_new_account_page import CreateAnAccountPage
#Временно


class TestCreateAnAccount:

    def test_create_an_account_good_info(self, fake_firstname , fake_lastname , fake_password , fake_email , driver):
        page = CreateAnAccountPage(driver)
        page.open()
        page.first_name_fill(fake_firstname)
        page.last_name_fill(fake_lastname)
        page.email_fill(fake_email)
        page.first_password_fill(fake_password)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.success_create_account_msg() == CreateAnAccountPageLocators.TEXT_THX_FOR_REGISTRATION_MSG , 'не удалось зарегаться с валидными данными '

    def test_create_an_account_without_firstname(self,fake_lastname , fake_password , fake_email , driver):
        page = CreateAnAccountPage(driver)
        page.open()
        page.last_name_fill(fake_lastname)
        page.email_fill(fake_email)
        page.first_password_fill(fake_password)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.error_firstname_not_filled() == CreateAnAccountPageLocators.TEXT_ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ИМЕНИ'

    def test_create_an_account_without_lastname(self,fake_firstname, fake_password , fake_email , driver):
        page = CreateAnAccountPage(driver)
        page.open()
        page.first_name_fill(fake_firstname)
        page.email_fill(fake_email)
        page.first_password_fill(fake_password)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.error_lastname_not_filled() == CreateAnAccountPageLocators.TEXT_ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ФАМИЛИИ'

    def test_create_an_account_without_email(self,fake_firstname, fake_lastname, fake_password , driver):
        page = CreateAnAccountPage(driver)
        page.open()
        page.first_name_fill(fake_firstname)
        page.last_name_fill(fake_lastname)
        page.first_password_fill(fake_password)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.error_email_not_filled() == CreateAnAccountPageLocators.TEXT_ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ EMAIL'

    def test_create_an_account_without_first_password(self,fake_firstname, fake_lastname, fake_password ,fake_email, driver):
        page = CreateAnAccountPage(driver)
        page.open()
        page.first_name_fill(fake_firstname)
        page.last_name_fill(fake_lastname)
        page.email_fill(fake_email)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.error_first_password_not_filled() == CreateAnAccountPageLocators.TEXT_ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ПАРОЛЯ'

    def test_create_an_account_without_confirm_password(self,fake_firstname, fake_lastname, fake_password ,fake_email, driver):
        page = CreateAnAccountPage(driver)
        page.create_account_without_second_password(page=page , email = fake_email , firstname= fake_firstname , lastname=fake_lastname, password=fake_password )
        assert page.error_confirm_password_not_filled_or_not_same_like_first() == CreateAnAccountPageLocators.TEXT_ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ВТОРОГО ПАРОЛЯ'

    def test_create_an_account_with_invalid_email(self,fake_firstname, fake_lastname, fake_password ,driver):
        page = CreateAnAccountPage(driver)
        page.create_account_with_invalid_email(page , password=fake_password,lastname=fake_lastname,firstname=fake_firstname)
        assert page.error_invalid_email() == CreateAnAccountPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE, 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕПРАВИЛЬНОГО ВИДА ЕМЕЙЛА'

    def test_create_an_account_with_wrong_second_password(self,fake_email,fake_firstname, fake_lastname, fake_password ,driver):
        page = CreateAnAccountPage(driver)
        page.create_account_with_wrong_second_password(page , password=fake_password,lastname=fake_lastname,firstname=fake_firstname, email=fake_email)
        assert page.error_confirm_password_not_filled_or_not_same_like_first() == CreateAnAccountPageLocators.TEXT_ERROR_MSG_SECOND_PASSWORD_WRONG, 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕСОВПАДЕНИЯ ПАРОЛЕЙ'


    # def test_enter_click(self, driver):
    #     page = CreateAnAccountPage(driver)
    #     page.open()
    #     page.search_items_field().click()
    #     page.search_items_field().send_keys('Enter')
    #     page.click_enter(page.search_items_field())