from selenium import webdriver # вебдрайвер импортируем
from selenium.webdriver.common.by import By # импорт библиотеку
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_modal_windows():
 driver = webdriver.Chrome()
 driver.get("https://the-internet.herokuapp.com/entry_ad")
 modal_windows = WebDriverWait(driver, 10). until (
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#modal > div.modal"))
)
 modal = modal_windows.find_element(By.CSS_SELECTOR, "#modal > div.modal > div.modal-title > h3")

 assert modal.text == "THIS IS A MODAL WINDOW"

 close_button = (modal_windows.find_element
                 (By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p"))
 close_button.click()

 is_closed = WebDriverWait(driver, 10).until(EC.invisibility_of_element(
     (By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p")))
 assert is_closed

 main_content = WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.CSS_SELECTOR, "#content"))
 )

 title = main_content.find_element(By.CSS_SELECTOR, "div.example > h3").text
 assert title == "Entry Ad"

 driver.quit()
