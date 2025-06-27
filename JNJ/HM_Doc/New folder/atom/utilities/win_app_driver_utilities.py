from selenium.webdriver.common.keys import Keys


def set_element_text(element, text: str):
    element.click()
    element.send_keys(Keys.CONTROL + "a" + Keys.CONTROL)
    element.send_keys(Keys.DELETE)
    element.send_keys(text)
