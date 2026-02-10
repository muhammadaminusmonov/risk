from pages.base_page import BasePage

class SignupPage(BasePage):

    def enter_name_and_email(self, name, email):
        self.page.fill("input[name='name']", name)
        self.page.fill("input[data-qa='signup-email']", email)
        self.page.click("button[data-qa='signup-button']")

    def fill_registration_form(self):
        self.page.check("input[id='id_gender1']")
        self.page.fill("input[id='password']", "test1234")
        self.page.fill("input[id='first_name']", "Test")
        self.page.fill("input[id='last_name']", "User")
        self.page.fill("input[id='address1']", "Test Address")
        self.page.select_option("select[id='country']", "India")
        self.page.fill("input[id='state']", "Test State")
        self.page.fill("input[id='city']", "Test City")
        self.page.fill("input[id='zipcode']", "12345")
        self.page.fill("input[id='mobile_number']", "1234567890")
        self.page.click("button[data-qa='create-account']")

    def confirm_account_created(self):
        return self.page.is_visible("text=Account Created!")
