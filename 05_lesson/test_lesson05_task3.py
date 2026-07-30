from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")
    sleep(3)

    assert len(links) == 9, \
        f"Expected 9 links, but found {len(links)}"

    for link in links:
        assert link.is_displayed()

    first_link = links[0]
    assert first_link.text == "1"

    driver.quit()
