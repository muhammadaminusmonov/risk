from pages.base_page import BasePage

class ProductsPage(BasePage):

    def add_first_product(self):
        self.page.hover(".product-image-wrapper")
        self.page.click("text=Add to cart")
        self.page.click("text=Continue Shopping")

    def add_second_product(self):
        self.page.hover("(//div[@class='product-image-wrapper'])[2]")
        self.page.click("(//a[text()='Add to cart'])[2]")
        self.page.click("text=View Cart")
