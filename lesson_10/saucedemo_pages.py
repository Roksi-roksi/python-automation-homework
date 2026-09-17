from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц магазина Swag Labs."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """Инициализирует веб-драйвер и общие локаторы."""
        self.driver: webdriver.Chrome = driver
        self.TITLE: tuple[str, str] = (By.CSS_SELECTOR, "span.title")

    def verify_page_title(self, expected_title: str) -> None:
        """
        Ожидает появление конкретного заголовка страницы и проверяет его.

        :param expected_title: Ожидаемый текст заголовка.
        :return: Ничего не возвращает (None).
        """
        # Сначала явно ждем появления нужного текста на странице
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.TITLE, expected_title)
        )
        actual_title: str = self.driver.find_element(*self.TITLE).text
        assert (
            actual_title == expected_title
        ), f"Ожидалась страница '{expected_title}', но мы на '{actual_title}'"


class LoginPage(BasePage):
    """Класс для взаимодействия со страницей авторизации."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """Инициализирует локаторы формы входа."""
        super().__init__(driver)
        self.url: str = "https://saucedemo.com"
        self.USERNAME_INPUT: tuple[str, str] = (By.ID, "user-name")
        self.PASSWORD_INPUT: tuple[str, str] = (By.ID, "password")
        self.LOGIN_BUTTON: tuple[str, str] = (By.ID, "login-button")

    def open(self) -> None:
        """Открывает главную страницу авторизации магазина."""
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в магазин под указанными учетными данными.

        :param username: Имя пользователя.
        :param password: Пароль.
        :return: Ничего не возвращает (None).
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class CatalogPage(BasePage):
    """Класс для взаимодействия со страницей каталога товаров."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """Инициализирует локаторы каталога."""
        super().__init__(driver)
        self.CART_LINK: tuple[str, str] = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_products_to_cart(self, product_ids: list[str]) -> None:
        """
        Добавляет список товаров в корзину по их уникальным ID кнопкам.

        :param product_ids: Список строк с ID кнопок добавления товаров.
        :return: Ничего не возвращает (None).
        """
        wait = WebDriverWait(self.driver, 10)
        for prod_id in product_ids:
            wait.until(EC.element_to_be_clickable((By.ID, prod_id))).click()

    def go_to_cart(self) -> None:
        """
        Осуществляет переход на страницу корзины.

        :return: Ничего не возвращает (None).
        """
        self.driver.find_element(*self.CART_LINK).click()


class CartPage(BasePage):
    """Класс для взаимодействия со страницей корзины покупателя."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """Инициализирует локаторы корзины."""
        super().__init__(driver)
        self.CHECKOUT_BUTTON: tuple[str, str] = (By.ID, "checkout")

    def proceed_to_checkout(self) -> None:
        """
        Нажимает кнопку перехода к оформлению заказа.

        :return: Ничего не возвращает (None).
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()


class CheckoutPage(BasePage):
    """Класс для взаимодействия со страницами оформления заказа."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """Инициализирует локаторы формы оформления заказа."""
        super().__init__(driver)
        self.FIRST_NAME: tuple[str, str] = (By.ID, "first-name")
        self.LAST_NAME: tuple[str, str] = (By.ID, "last-name")  # Опечатка исправлена!
        self.POSTAL_CODE: tuple[str, str] = (By.ID, "postal-code")

        self.CONTINUE_BUTTON: tuple[str, str] = (By.ID, "continue")
        self.TOTAL_LABEL: tuple[str, str] = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_checkout_info(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет персональные данные покупателя для оформления доставки.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        :return: Ничего не возвращает (None).
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LAST_NAME)
        ).send_keys(last_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        ).send_keys(postal_code)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def verify_total_price(self, expected_total: str) -> None:
        """
        Сверяет итоговую стоимость заказа (включая налоги) с ожидаемой.

        :param expected_total: Ожидаемая финальная сумма строкой.
        :return: Ничего не возвращает (None).
        """
        actual_total: str = (
            WebDriverWait(self.driver, 10)
            .until(EC.visibility_of_element_located(self.TOTAL_LABEL))
            .text
        )
        print(f"\nИтоговая стоимость в магазине: {actual_total}")
        assert (
            actual_total == expected_total
        ), f"Ожидалось '{expected_total}', но отображается '{actual_total}'"
