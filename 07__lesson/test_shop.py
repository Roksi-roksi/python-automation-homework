from selenium import webdriver
from saucedemo__pages import LoginPage, CatalogPage, CartPage, CheckoutPage


def test_shop_flow():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    catalog_page = CatalogPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        catalog_page.verify_page_title("Products")

        products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        catalog_page.add_products_to_cart(products)
        catalog_page.go_to_cart()

        cart_page.verify_page_title("Your Cart")

        cart_page.proceed_to_checkout()
        checkout_page.fill_checkout_info("Roks", "Remi", "123456")

        checkout_page.verify_page_title("Checkout: Overview")

        checkout_page.verify_total_price("Total: $58.29")

    finally:
        driver.quit()


