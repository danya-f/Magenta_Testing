from selenium.webdriver.common.by import By


(By.XPATH,"//a[@href='https://softwaretestingboard.com/write-for-us/']")
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





    # КНОПКИ
    SEARCH_FIELD = (By.XPATH, "//*[@id = 'search']")


class MainPageLocators:







class SignInPageLocators:
    EMAIL_FIELD = (By.XPATH , "//*[@id = 'email']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id = 'pass']")