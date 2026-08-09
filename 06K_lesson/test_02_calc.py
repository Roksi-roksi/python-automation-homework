from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(
            By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)"
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)"
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)"
        ).click()

        driver.find_element(
            By.CSS_SELECTOR,
            "#calculator > div.keys > span.btn.btn-outline-warning",
        ).click()

        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        final_result = driver.find_element(By.CLASS_NAME, "screen").text
        assert (
            final_result == "15"
        ), f"Ожидался результат '15', но на экране '{final_result}'"

    finally:
        driver.quit()