from app.ui.login import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class HomeElements:
    SELECT_SORT = (By.XPATH, "//select[@class='product_sort_container']")
    PRICE_BAR = (By.XPATH, "//div[@class='pricebar']")

class Home(Login):
    def sort_page(self, select_by):
        items = Select(self.driver.find_element(*HomeElements.SELECT_SORT))
        items.select_by_visible_text(select_by)
    # def verify_sorting(self, first_price):
    #     is_sorted_correctly = False
    #     prices = self.driver.find_elements(*HomeElements.RICE_BAR)
    #     if first_price in 