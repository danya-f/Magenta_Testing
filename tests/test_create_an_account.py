from data.urls import CREATE_ACCOUNT_PAGE_URL , THX_FOR_REGISTRATION_MSG , ERROR_MSG_INVALID_EMAIL, ERROR_MSG_FIELD_FILL
from pages.create_new_account_page import CreateAnAccountPage

class TestCreateAnAccount:

    def test_create_an_account_good_info(self, fake_firstname , fake_lastname , fake_password , fake_email , driver):
        page = CreateAnAccountPage(driver , CREATE_ACCOUNT_PAGE_URL)
        page.open()
        page.first_name_fill(fake_firstname)
        page.last_name_fill(fake_lastname)
        page.email_fill(fake_email)
        page.first_password_fill(fake_password)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.success_create_account_msg() == THX_FOR_REGISTRATION_MSG , 'не удалось зарегаться с валидными данными '

    def test_create_an_account_without_firstname(self,fake_lastname , fake_password , fake_email , driver):
        page = CreateAnAccountPage(driver , CREATE_ACCOUNT_PAGE_URL)
        page.open()
        page.last_name_fill(fake_lastname)
        page.email_fill(fake_email)
        page.first_password_fill(fake_password)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.error_firstname_not_filled() == ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ИМЕНИ'

    def test_create_an_account_without_lastname(self,fake_firstname, fake_password , fake_email , driver):
        page = CreateAnAccountPage(driver , CREATE_ACCOUNT_PAGE_URL)
        page.open()
        page.first_name_fill(fake_firstname)
        page.email_fill(fake_email)
        page.first_password_fill(fake_password)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.error_lastname_not_filled() == ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ФАМИЛИИ'

    def test_create_an_account_without_email(self,fake_firstname, fake_lastname, fake_password , driver):
        page = CreateAnAccountPage(driver , CREATE_ACCOUNT_PAGE_URL)
        page.open()
        page.first_name_fill(fake_firstname)
        page.last_name_fill(fake_lastname)
        page.first_password_fill(fake_password)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.error_email_not_filled() == ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ EMAIL'

    def test_create_an_account_without_first_password(self,fake_firstname, fake_lastname, fake_password ,fake_email, driver):
        page = CreateAnAccountPage(driver , CREATE_ACCOUNT_PAGE_URL)
        page.open()
        page.first_name_fill(fake_firstname)
        page.last_name_fill(fake_lastname)
        page.email_fill(fake_email)
        page.confirm_password_fill(fake_password)
        page.create_an_account_button_click()
        assert page.error_first_password_not_filled() == ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ПАРОЛЯ'

    def test_create_an_account_without_confirm_password(self,fake_firstname, fake_lastname, fake_password ,fake_email, driver):
        page = CreateAnAccountPage(driver , CREATE_ACCOUNT_PAGE_URL)
        page.create_account_without_second_password(page=page , email = fake_email , firstname= fake_firstname , lastname=fake_lastname, password=fake_password )
        assert page.error_confirm_password_not_filled() == ERROR_MSG_FIELD_FILL , 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ВТОРОГО ПАРОЛЯ'

    def test_create_an_account_with_invalid_email(self,fake_firstname, fake_lastname, fake_password ,driver):
        page = CreateAnAccountPage(driver , CREATE_ACCOUNT_PAGE_URL)
        page.create_account_with_invalid_email(page , password=fake_password,lastname=fake_lastname,firstname=fake_firstname)
        assert page.error_invalid_email() == ERROR_MSG_INVALID_EMAIL, 'НЕ ПОЯВИЛСЯ ТЕКСТ ЕРРОРА ИЗ ЗА НЕЗАПОЛНЕНИЯ ВТОРОГО ПАРОЛЯ'
