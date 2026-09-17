import time
import allure
from selenium import webdriver
from saucedemo_pages import LoginPage, CatalogPage, CartPage, CheckoutPage


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Сквозной сценарий покупки товаров в магазине Swag Labs")
@allure.description(
    "Тест авторизуется, добавляет три товара в корзину, "
    "оформляет заказ и проверяет финальную стоимость."
)
def test_shop_flow() -> None:
    driver = webdriver.Chrome()
    driver.maximize_window()

    login_page = LoginPage(driver)
    catalog_page = CatalogPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    try:
        with allure.step("Открыть страницу авторизации"):
            login_page.open()

        with allure.step("Авторизоваться под пользователем standard_user"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Проверить успешный переход в каталог"):
            catalog_page.verify_page_title("Products")

        with allure.step("Добавить выбранные товары в корзину"):
            products = [
                "add-to-cart-sauce-labs-backpack",
                "add-to-cart-sauce-labs-bolt-t-shirt",
                "add-to-cart-sauce-labs-onesie",
            ]
            catalog_page.add_products_to_cart(products)

        with allure.step("Перейти в корзину"):
            catalog_page.go_to_cart()

        with allure.step("Проверить, что мы находимся в корзине"):
            cart_page.verify_page_title("Your Cart")

        with allure.step("Нажать на кнопку Checkout"):
            cart_page.proceed_to_checkout()

        with allure.step("Заполнить форму оформления заказа"):
            checkout_page.fill_checkout_info(
                first_name="Roks", last_name="Remi", postal_code="123456"
            )
        with allure.step("Ожидание обновления страницы сайтом"):
            time.sleep(2)

        with allure.step("Проверить переход на страницу проверки заказа"):
            checkout_page.verify_page_title("Checkout: Overview")

        with allure.step("Проверить, что итоговая сумма равна $58.29"):
            checkout_page.verify_total_price("Total: $58.29")

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()
