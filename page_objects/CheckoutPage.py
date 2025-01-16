from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self,driver):
        self.driver= driver


    checkout_button = (By.XPATH, "//div[@class='cart-preview active']//button[contains(text(),'PROCEED TO CHECKOUT')]")

    def click_final_checkout_button(self):
        self.driver.find_element(*CheckoutPage.checkout_button).click()
