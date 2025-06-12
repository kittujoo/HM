from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

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

def youTube_search():
    driver = setup_driver()
    try:
        # Open YouTube
        driver.get("https://www.youtube.com")

        # Wait for page to load with WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC    
        from selenium.webdriver.support.ui import WebDriverWait
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "search_query")))
        for text in ["Python Selenium Tutorial", "Web Automation with Selenium"]:
            # Find the search box and enter text
            search_box = driver.find_element(By.NAME, "search_query")
            search_box.clear()
            # Find the search box and enter text
            search_box = driver.find_element(By.NAME, "search_query")
            search_box.send_keys(text)
            search_box.send_keys(Keys.RETURN)  # Press Enter key
            
            # Wait for results to load
            time.sleep(3)
            # Take screenshot
            driver.save_screenshot(f"youtube_search_result_{text}.png")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
        
        
        
if __name__ == "__main__":
    youTube_search()