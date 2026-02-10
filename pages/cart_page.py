from pages.base_page import BasePage

class CartPage(BasePage):

    def check_products_in_cart(self):
        products = self.page.locator(".cart_description")
        return products.count()

    def proceed_to_checkout(self):
        self.page.click("text=Proceed To Checkout")
