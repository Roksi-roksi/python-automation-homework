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

    current_url = driver.current_url
    assert "/forms/post" in current_url
    sleep(3)

    driver.back()
    sleep(5)

    final_url = driver.current_url
    assert final_url == "https://httpbin.qa-territory.online/"
    sleep(3)

    










    driver.quit()