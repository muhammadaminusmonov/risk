from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def place_order(self):
        self.page.fill("textarea[name='message']", "Test order")
        self.page.click("text=Place Order")

    def enter_payment_details(self):
        self.page.fill("input[name='name_on_card']", "Test User")
        self.page.fill("input[name='card_number']", "4111111111111111")
        self.page.fill("input[name='cvc']", "123")
        self.page.fill("input[name='expiry_month']", "12")
        self.page.fill("input[name='expiry_year']", "2028")
        self.page.click("button[id='submit']")

    def confirm_order(self):
        return self.page.is_visible("text=Order Placed!")
