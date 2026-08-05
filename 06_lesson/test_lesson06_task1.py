from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    finish_text_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    driver.save_screenshot("06_lesson/screenshots/dynamic_loading.png")

    assert finish_text_element.text == "Hello World!"
