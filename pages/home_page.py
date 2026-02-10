from pages.base_page import BasePage

class HomePage(BasePage):

    def open_signup_page(self):
        self.page.click("text=Signup / Login")

    def open_products_page(self):
        self.page.click("text=Products")
