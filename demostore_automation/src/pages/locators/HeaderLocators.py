
from selenium.webdriver.common.by import By

class HeaderLocators:

    CART_RIGHT_HEADER = (By.ID, 'site-header-cart')
    CART_ITEM_COUNT = (By.CSS_SELECTOR, 'li a.cart-contents span.count')
    MENU_ITEMS = (By.CSS_SELECTOR, 'div.menu ul.nav-menu li')