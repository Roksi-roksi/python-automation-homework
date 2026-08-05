from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_gitflic_user_profile(driver):
    driver.get("https://gitflic.ru/")

    user_cookie = {
        "name": "SESSION",
        "value": "ZjE0N2UyZWUtMGYwYS00YTlkLWE5NDUtN2Q4ZjVjYWFkYzk1",
    }
    driver.add_cookie(user_cookie)
    driver.refresh()

    driver.get("https://gitflic.ru/user/myrtia9758")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), '@myrtia9758')]")
        )
    )
    driver.save_screenshot("06_lesson/screenshots/user_1_profile.png")

    url_user_1 = driver.current_url
    driver.delete_all_cookies()
    driver.refresh()

    cookie_user_2 = {
        "name": "SESSION",
        "value": "OGNjNzI1NGQtMzM4Zi00YTQyLTg0ZGYtMGI4YjBhNjA2NmE5",
    }
    driver.add_cookie(cookie_user_2)
    driver.refresh()

    driver.get("https://gitflic.ru/user/roksweb")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), '@roksweb')]")
        )
    )
    driver.save_screenshot("06_lesson/screenshots/user_2_profile.png")

    url_user_2 = driver.current_url

    assert url_user_1 != url_user_2
