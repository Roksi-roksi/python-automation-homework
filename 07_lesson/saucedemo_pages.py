from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.TITLE = (By.CSS_SELECTOR, "span.title")

    def _get_title_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE)
        ).text

    def verify_page_title(self, expected_title: str):
        actual_title = self._get_title_text()
        assert actual_title == expected_title, f"Ожидалась страница '{expected_title}', но мы на '{actual_title}'"


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://saucedemo.com"
        self.USERNAME_INPUT = (By.ID, "user-name")
        self.PASSWORD_INPUT = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class CatalogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_products_to_cart(self, product_names: list):
        wait = WebDriverWait(self.driver, 10)
        for name in product_names:
            wait.until(EC.element_to_be_clickable((By.NAME, name))).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.CHECKOUT_BUTTON = (By.ID, "checkout")

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.FIRST_NAME = (By.ID, "first-name")
        self.LAST_NAME = (By.ID, "last-name")
        self.POSTAL_CODE = (By.ID, "postal-code")
        self.CONTINUE_BUTTON = (By.ID, "continue")
        self.TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def verify_total_price(self, expected_total: str):
        actual_total = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        ).text
        print(f"\nИтоговая стоимость в магазине: {actual_total}")
        assert actual_total == expected_total, f"Ожидалось '{expected_total}', но отображается '{actual_total}'"

