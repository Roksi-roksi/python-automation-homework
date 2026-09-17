from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для взаимодействия со страницей калькулятора."""

    def __init__(self, driver: webdriver.Chrome) -> None:
        """Инициализирует веб-драйвер и локаторы элементов страницы."""
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.DELAY_INPUT = (By.ID, "delay")
        self.SCREEN = (By.CLASS_NAME, "screen")

    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get(self.url)

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку выполнения операции в секундах.

        :param seconds: Количество секунд ожидания в виде строки.
        """
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(seconds)

    def _click_button(self, button_text: str) -> None:
        """
        Внутренний метод для клика по кнопке калькулятора по её тексту.

        :param button_text: Текст на кнопке (например, '7', '+', '=').
        """
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    def enter_expression(self, expression: str) -> None:
        """
        Вводит математическое выражение, последовательно нажимая кнопки.

        :param expression: Строка выражения, например "7+8=".
        """
        for char in expression:
            self._click_button(char)

    def verify_result(self, expected_result: str, timeout: int = 55) -> None:
        """
        Ожидает появление результата на экране и сверяет его с ожидаемым.

        :param expected_result: Ожидаемый результат в виде строки.
        :param timeout: Максимальное время ожидания ответа в секундах.
        :raises AssertionError: Если итоговый текст не совпадает с ожидаемым.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )

        actual_result = self.driver.find_element(*self.SCREEN).text
        assert actual_result == expected_result, (
            f"Ожидался результат '{expected_result}', "
            f"но на экране отобразилось: '{actual_result}'"
        )
