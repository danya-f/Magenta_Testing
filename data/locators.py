from selenium.webdriver.common.by import By



(By.XPATH,"")
(By.XPATH,"")
(By.XPATH,"")
(By.XPATH,"")
(By.XPATH,"")
(By.XPATH,"")




class GeneralLocators:
    # ПЕРЕХОДЫ
    SIGNIN_LINK = (By.XPATH, "//div[@class='panel header']//*[@data-label='or']")
    CREATE_ACCOUNT_LINK = (By.XPATH,"//div[@class='panel header']//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']")
    CART_LINK = (By.XPATH, "//*[@class = 'action showcart']")
    #MAIN_CATALOG_LINKS
    WHATS_NEW_LINK = (By.XPATH, "//li[@class='level0 nav-1 category-item first level-top ui-menu-item']")
    WOMAN_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-2 category-item active level-top parent ui-menu-item']")
    MAN_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-3 category-item level-top parent ui-menu-item']")
    GEAR_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-4 category-item level-top parent ui-menu-item']")
    TRAINING_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-5 category-item level-top parent ui-menu-item']")
    SALE_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-6 category-item last level-top ui-menu-item']")

    #DOWN_CATALOG_LINKS
    SEARCH_TERMS_LINK = (By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/search/term/popular/']")
    PRIVACY_AND_COOKIE_POLICY_LINK = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode/']")
    ADVANCED_SEARCH_LINK = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/catalogsearch/advanced/']")
    ORDERS_AND_RETURNS__LINK = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/sales/guest/form/']")

    # КНОПКИ
    SEARCH_FIELD = (By.XPATH, "//*[@id = 'search']")



class SignInPageLocators:
    #ПОЛЯ ДЛЯ ЗАПОЛНЕНИЯ
    EMAIL_FIELD = (By.XPATH , "//*[@id = 'email']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id = 'pass']")

    #ПЕРЕХОДЫ
    CREATE_AN_ACCOUNT_FROM_SIGNIN_LINK = (By.XPATH , "//*[@class='action create primary']")


    #КНОПКИ
    SIGN_IN_BUTTON = (By.XPATH, "//button[@id='send2' and @class='action login primary']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[@class='action remind']")


class CreateAnAccountPageLocators:
    #ПОЛЯ ДЛЯ ЗАПОЛНЕНИЯ
    FIRST_NAME_FIELD = (By.XPATH, "//*[@id = 'firstname']")
    LAST_NAME_FIELD = (By.XPATH, "//*[@id = 'lastname']")
    EMAIL_FIELD = (By.XPATH , "//*[@id = 'email_address']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id = 'password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//*[@id = 'password-confirmation']")

    #ПЕРЕХОДЫ
    CREATE_AN_ACCOUNT_FROM_SIGNIN_LINK = (By.XPATH , "//*[@class='action create primary']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@title='Create an Account']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@id='send2' and @class='action login primary']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[@class='action remind']")

