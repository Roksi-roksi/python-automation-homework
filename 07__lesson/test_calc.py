from selenium import webdriver
from calculator__page import CalculatorPage

def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    calc_page = CalculatorPage(driver)

    try:
        calc_page.open()
        calc_page.set_delay("45")
        calc_page.enter_expression("7+8=")
        calc_page.verify_result("15", timeout=55)

    finally:
        driver.quit()


