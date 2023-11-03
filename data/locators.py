from selenium.webdriver.common.by import By

class BasePageLocators:
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
    ORDERS_AND_RETURNS_LINK = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/sales/guest/form/']")

    # КНОПКИ
    SEARCH_FIELD = (By.XPATH, "//*[@id = 'search']")


# class AnyPageLocators:
#     # ПЕРЕХОДЫ
#     SIGNIN_LINK = (By.XPATH, "//div[@class='panel header']//*[@data-label='or']")
#     CREATE_ACCOUNT_LINK = (By.XPATH,"//div[@class='panel header']//a[@href='https://magento.softwaretestingboard.com/customer/account/create/']")
#     CART_LINK = (By.XPATH, "//*[@class = 'action showcart']")
#     #MAIN_CATALOG_LINKS
#     WHATS_NEW_LINK = (By.XPATH, "//li[@class='level0 nav-1 category-item first level-top ui-menu-item']")
#     WOMAN_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-2 category-item active level-top parent ui-menu-item']")
#     MAN_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-3 category-item level-top parent ui-menu-item']")
#     GEAR_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-4 category-item level-top parent ui-menu-item']")
#     TRAINING_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-5 category-item level-top parent ui-menu-item']")
#     SALE_ITEMS_LINK = (By.XPATH, "//li[@class='level0 nav-6 category-item last level-top ui-menu-item']")
#
#     #DOWN_CATALOG_LINKS
#     SEARCH_TERMS_LINK = (By.XPATH,"//a[@href='https://magento.softwaretestingboard.com/search/term/popular/']")
#     PRIVACY_AND_COOKIE_POLICY_LINK = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode/']")
#     ADVANCED_SEARCH_LINK = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/catalogsearch/advanced/']")
#     ORDERS_AND_RETURNS_LINK = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/sales/guest/form/']")
#
#     # КНОПКИ
#     SEARCH_FIELD = (By.XPATH, "//*[@id = 'search']")



class SignInPageLocators:
    #ПОЛЯ ДЛЯ ЗАПОЛНЕНИЯ
    EMAIL_FIELD = (By.XPATH , "//*[@id = 'email']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id = 'pass']")

    #ПЕРЕХОДЫ
    CREATE_AN_ACCOUNT_FROM_SIGNIN_PAGE = (By.XPATH , "//*[@class='action create primary']")


    #КНОПКИ
    SIGN_IN_BUTTON = (By.XPATH, "//button[@id='send2' and @class='action login primary']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[@class='action remind']")

    #MESSAGE
    ERROR_SIGNIN_MSG = (By.XPATH,"//*[@data-bind= 'html: $parent.prepareMessageForHtml(message.text)']")

    TEXT_ERROR_SIGNIN_MSG = "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."


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

    # #MSG
    ERROR_FIRSTNAME_FIELD = (By.XPATH , "//*[@id='firstname-error']")
    ERROR_LASTNAME_FIELD = (By.XPATH, "//*[@id='lastname-error']")
    ERROR_EMAIL_FIELD = (By.XPATH, "//*[@id='email_address-error']")
    ERROR_FIRST_PASSWORD_FIELD = (By.XPATH, "//*[@id='password-error']")
    ERROR_CONFIRM_PASSWORD_FIELD = (By.XPATH, "//*[@id='password-confirmation-error']")

    TEXT_THX_FOR_REGISTRATION_MSG = "Thank you for registering with Main Website Store."
    TEXT_ERROR_MSG_FIELD_FILL = "This is a required field."
    TEXT_ERROR_MESSAGE_EMAIL_TYPE = "Please enter a valid email address (Ex: johndoe@domain.com)."
    TEXT_ERROR_MSG_SECOND_PASSWORD_WRONG = "Please enter the same value again."






class MyAccountPageLocators:
    MY_ACCOUNT_MSG_THX_FOR_REGISTRATION = (By.XPATH,"//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")

    MY_ACCOUNT_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[1]")
    MY_ORDERS_BUTTON = (By.XPATH,"(//ul[@class='nav items']/li)[2]")
    MY_DOWNLOADABLE_PRODUCTS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[3]")
    MY_WISH_LIST_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[4]")
    ADDRESS_BOOK_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[6]")
    ACCOUNT_INFORMATION_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[7]")
    STORED_PAYMENT_METHODS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[8]")
    MY_PRODUCT_REVIEWS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[10]")


class OrdersAndReturnsPageLocators:
    ORDER_ID_FIELD = (By.XPATH, "//*[@id='oar-order-id']")
    ORDER_ID_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar-order-id-error']")

    BILLING_LASTNAME_FIELD = (By.XPATH, "//*[@id='oar-billing-lastname']")
    BILLING_LASTNAME_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar-billing-lastname-error']")

    FIND_ORDER_BY_DROPDOWN = (By.XPATH,"//*[@id='quick-search-type-id']")
    FIND_ORDER_BY_EMAIL_DROPDOWN = (By.XPATH,"//option[@value='email']")
    FIND_ORDER_BY_ZIP_CODE_DROPDOWN = (By.XPATH, "//option[@value='zip']")

    EMAIL_FIELD = (By.XPATH,"//*[@id='oar_email']")
    EMAIL_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar_email-error']")
    LABEL_EMAIL_FIELD = (By.XPATH,"//label[@for='oar_email']")

    ZIP_FIELD = (By.XPATH,"//*[@id='oar_zip']")
    ZIP_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar_zip-error']")
    LABEL_ZIP_FIELD = (By.XPATH, "//label[@for='oar_zip']")

    CONTINUE_BUTTON = (By.XPATH, "//*[@title='Continue']")

    TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD = "This is a required field."
    TEXT_ERROR_MESSAGE_EMAIL_TYPE = "Please enter a valid email address (Ex: johndoe@domain.com)."
    TEXT_LABEL_ZIP_FIELD = "Billing ZIP Code"
    TEXT_LABEL_EMAIL_FIELD = "Email"







