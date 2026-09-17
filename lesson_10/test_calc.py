import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@allure.title("Проверка калькулятора с задержкой")
@allure.description("Тест проверяет корректность вычислений калькулятора при установленной задержке работы в 45 секунд.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator() -> None:
    driver = webdriver.Chrome()
    driver.maximize_window()
    calc_page = CalculatorPage(driver)

    try:
        with allure.step("Открыть страницу калькулятора"):
            calc_page.open()

        with allure.step("Установить задержку вычислений в 45 секунд"):
            calc_page.set_delay("45")

        with allure.step("Ввести математическое выражение '7 + 8 ='"):
            calc_page.enter_expression("7+8=")

        with allure.step("Проверить, что через 45 секунд результат равен '15'"):
            calc_page.verify_result(expected_result="15", timeout=55)

    finally:
        with allure.step("Закрыть браузер"):
            driver.quit()
