from page_objects.CheckoutPage import CheckoutPage
from page_objects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):


    def test_e2e(self):


        log= self.getLogger()
        home_page= HomePage(self.driver)

        log.info("selecting all products in the home page")
        home_page.search_action()
        home_page.click_on_all_products()
        home_page.cart_button()

        # Proceed to cart and checkout
        log.info("checking out all products")
        checkout_page = CheckoutPage(self.driver)
        checkout_page.click_final_checkout_button()
