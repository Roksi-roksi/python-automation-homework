from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://saucedemo.com")

        username_field = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        catalog_title_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.title"))
        )
        assert catalog_title_element.text == "Products"

        wait.until(
            EC.element_to_be_clickable(
                (By.NAME, "add-to-cart-sauce-labs-backpack")
            )
        ).click()
        driver.find_element(
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        cart_title_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.title"))
        )
        assert cart_title_element.text == "Your Cart"

        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        first_name_field = wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("john")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        overview_title_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.title"))
        )
        assert overview_title_element.text == "Checkout: Overview"

        total_summary_element = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        total_summary = total_summary_element.text

        print(f"\nИтоговая стоимость в магазине: {total_summary}")
        assert (
            total_summary == "Total: $58.29"
        ), f"Ожидалось 'Total: $58.29', но отображается '{total_summary}'"

    finally:
        driver.quit()


