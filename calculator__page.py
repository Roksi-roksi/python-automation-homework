from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.DELAY_INPUT = (By.ID, "delay")
        self.SCREEN = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(seconds)

    def _click_button(self, button_text: str):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*button_locator).click()

    def enter_expression(self, expression: str):
        for char in expression:
            self._click_button(char)

    def verify_result(self, expected_result: str, timeout: int = 55):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_result)
        )

        actual_result = self.driver.find_element(*self.SCREEN).text
        assert actual_result == expected_result, (
            f"Ожидался результат '{expected_result}', "
            f"но на экране отобразилось: '{actual_result}'"
        )

