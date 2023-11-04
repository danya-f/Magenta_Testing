from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from random import randint

fake = Faker()


@pytest.fixture()
def language():
    language = 'en'
    yield language


@pytest.fixture()
def options(language):
    options = Options()
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", {'intl.accept_languages': language})
    options.add_argument('--start-maximized')
    return options


@pytest.fixture()
def fake_password():
    fake_password = fake.password()
    return fake_password

@pytest.fixture()
def fake_firstname():
    fake_firstname = fake.first_name()
    return fake_firstname

@pytest.fixture()
def fake_lastname():
    fake_lastname = fake.last_name()
    return fake_lastname


@pytest.fixture()
def fake_email():
    fake_email = fake.email()
    return fake_email


@pytest.fixture()
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=30)
    return wait


@pytest.fixture()
def good_email():
    good_email = 'danyldyk2@mail.ru'
    return good_email

@pytest.fixture()
def incorrect_type_email():
    good_email = 'danyldyk2mail.ru'
    return good_email


@pytest.fixture()
def good_password():
    good_password = 'Palevo1999'
    return good_password


@pytest.fixture()
def fake_order_id():
    fake_order_id = randint(111111111,999999999)
    return fake_order_id


@pytest.fixture()
def fake_zip_code():
    fake_zip_code = fake.postcode()
    return fake_zip_code

