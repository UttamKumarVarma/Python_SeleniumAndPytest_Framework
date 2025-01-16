import time

from selenium.webdriver.common.by import By


class HomePage:


    #constructor
    def __init__(self, driver):
        self.driver = driver


    #locators
    search = (By.XPATH,"//input[@type='search']")
    all_products = (By.XPATH, "//div[@class='product-action']")
    checkout_button= (By.XPATH,"//img[@alt='Cart']")


    #methods
    def search_action(self):
        self.driver.find_element(*HomePage.search).click()

    def click_on_all_products(self):
        for product in self.driver.find_elements(*HomePage.all_products):
            product.click()
        time.sleep(2)

    def cart_button(self):
        self.driver.find_element(*HomePage.checkout_button).click()