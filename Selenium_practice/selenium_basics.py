# selenium_basics_to_advanced.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pytest

# -------- Setup and Basic Browser Actions --------
def setup_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Edge(options=options)
    # driver = webdriver.Firefox(options=options)
    # driver = webdriver.Safari(options=options)
    # driver = webdriver.Ie(options=options)
    # driver = webdriver.Opera(options=options)
    # driver = webdriver.PhantomJS(options=options)   
    # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
    # driver.get("https://www.google.com")
    
    driver.implicitly_wait(10)
    # driver.set_page_load_timeout(30)
    driver.maximize_window()
    return driver

# -------- Basic Navigation --------
def test_open_google():
    driver = setup_driver()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()

# -------- Finding and Interacting with Elements --------
def test_google_search():
    driver = setup_driver()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Selenium" in driver.title
    driver.quit()

# -------- Dropdown Handling --------
def test_select_dropdown():
    driver = setup_driver()
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
    driver.switch_to.frame("iframeResult")
    dropdown = Select(driver.find_element(By.ID, "cars"))
    dropdown.select_by_visible_text("Saab")
    time.sleep(1)
    driver.quit()

# -------- Handling Alerts --------
def test_alert_handling():
    driver = setup_driver()
    driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
    driver.switch_to.frame("iframeResult")
    driver.find_element(By.TAG_NAME, "button").click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.quit()

# -------- Handling Frames and Windows --------
def test_switch_window():
    driver = setup_driver()
    driver.execute_script("window.open('https://www.google.com');")
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    assert "Google" in driver.title
    driver.quit()

# -------- Mouse and Keyboard Actions --------
def test_mouse_hover():
    driver = setup_driver()
    driver.get("https://demoqa.com/menu")
    menu = driver.find_element(By.LINK_TEXT, "Main Item 2")
    actions = ActionChains(driver)
    actions.move_to_element(menu).perform()
    time.sleep(2)
    driver.quit()

# -------- Screenshot --------
def test_screenshot():
    driver = setup_driver()
    driver.get("https://www.google.com")
    driver.save_screenshot("google_homepage.png")
    driver.quit()

# -------- Example using Pytest --------
@pytest.mark.parametrize("search_term", ["Selenium", "Python", "WebDriver"])
def test_search_multiple_terms(search_term):
    driver = setup_driver()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.title_contains(search_term))
    assert search_term in driver.title
    driver.quit()

if __name__ == "__main__":
    # Run all tests
    # pytest.main([__file__])
    
    test_open_google()
    test_google_search()
    test_select_dropdown()
    test_alert_handling()
    test_switch_window()
    test_mouse_hover()
    test_screenshot()
    test_search_multiple_terms("Selenium")
    test_search_multiple_terms("Python")
    test_search_multiple_terms("WebDriver")