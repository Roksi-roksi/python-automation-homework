from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.qa-territory.online/")
    driver.maximize_window()
    sleep(5)

    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()
    sleep(5)


    custname = driver.find_element(By.NAME, "custname")
    custname.send_keys("Рокс Р")
    sleep(3)

    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    sleep(3)

    url_after_submit = driver.current_url

    expected_final_url = "https://httpbin.qa-territory.online/post"
    assert url_after_submit == expected_final_url, \
        f"Ожидался URL {expected_final_url}, сменился {url_after_submit}"

    driver.quit()