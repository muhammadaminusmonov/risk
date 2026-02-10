import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_full_purchase_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        home = HomePage(page)
        signup = SignupPage(page)
        products = ProductsPage(page)
        cart = CartPage(page)
        checkout = CheckoutPage(page)

        home.open("https://www.automationexercise.com")
        home.open_signup_page()

        signup.enter_name_and_email("TestUser", "testuser123@email.com")
        signup.fill_registration_form()
        assert signup.confirm_account_created()

        home.open_products_page()
        products.add_first_product()
        products.add_second_product()

        assert cart.check_products_in_cart() == 2
        cart.proceed_to_checkout()

        checkout.place_order()
        checkout.enter_payment_details()
        assert checkout.confirm_order()

        browser.close()
