from selenium import webdriver # вебдрайвер импортируем
from selenium.webdriver.common.by import By # импорт библиотеку
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    button = WebDriverWait(driver, 10).until (
    EC. element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
    button.click()

    message_element = WebDriverWait(driver, 10).until (
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#message")))

    assert message_element.text == "It's gone!"

    enable_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))
    enable_button.click()

    input_wait = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > input")))
    input_wait.send_keys("click")

    assert input_wait.get_attribute("value") == "click"

    driver.quit()
