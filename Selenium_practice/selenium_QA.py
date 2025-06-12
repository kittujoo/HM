# selenium_interview_questions_with_answers.py

"""
Selenium Interview Questions and Answers
"""

# 1. What is Selenium?
"""
Selenium is an open-source automation tool for testing web applications across different browsers and platforms. It supports multiple programming languages like Java, Python, C#, etc.
"""

# 2. What are the components of Selenium?
"""
- Selenium IDE: A Chrome/Firefox plugin for recording and playing back tests.
- Selenium RC (deprecated): Older version allowing remote control.
- Selenium WebDriver: Modern framework for automating browsers using programming.
- Selenium Grid: Used for parallel test execution across multiple machines/browsers.
"""

# 3. What are the limitations of Selenium?
"""
- Cannot test desktop applications
- Cannot test mobile apps directly
- No built-in reporting
- Cannot handle CAPTCHA
"""

# 4. What programming languages does Selenium support?
"""
- Java
- Python
- C#
- Ruby
- JavaScript
- Kotlin
"""

# 5. What types of testing can you perform with Selenium?
"""
- Functional Testing
- Regression Testing
- Cross-browser Testing
"""

# 6. What browsers are supported by Selenium WebDriver?
"""
- Chrome
- Firefox
- Edge
- Safari
- Internet Explorer (legacy)
- Opera
"""

# 7. How do you find elements in Selenium?
"""
Using locators:
- By.ID
- By.NAME
- By.XPATH
- By.CSS_SELECTOR
- By.CLASS_NAME
- By.LINK_TEXT
- By.TAG_NAME
"""

# 8. Difference between findElement() and findElements()?
"""
- findElement(): Returns a single WebElement or throws NoSuchElementException
- findElements(): Returns a list of elements or empty list if not found
"""

# 9. How do you handle dropdowns in Selenium?
"""
Using the Select class:
```python
Select(driver.find_element(By.ID, 'dropdown')).select_by_visible_text('Option')
```
"""

# 10. How do you perform mouse and keyboard actions?
"""
Using ActionChains:
```python
ActionChains(driver).move_to_element(element).click().perform()
```
"""

# 11. Types of waits in Selenium?
"""
- Implicit Wait
- Explicit Wait
- Fluent Wait
"""

# 12. When would you use WebDriverWait over ImplicitWait?
"""
When you want to wait for a specific condition like element to be clickable.
```python
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'submit')))
```
"""

# 13. Difference between XPath and CSS Selector?
"""
- XPath supports navigating backward in DOM; CSS doesn't.
- CSS is generally faster.
"""

# 14. Absolute vs Relative XPath?
"""
- Absolute: Starts from root (`/html/body/...`)
- Relative: Starts from current or anywhere (`//div[@id='xyz']`)
"""

# 15. Fastest locator?
"""
ID is the fastest and most reliable.
"""

# 16. Have you worked with POM?
"""
Yes. Page Object Model abstracts page details into separate classes for maintainability.
"""

# 17. How do you handle reusable components?
"""
Create helper functions or base classes for common actions like login, waits, etc.
"""

# 18. Selenium project structure?
"""
- tests/
- pages/
- utils/
- conftest.py
- requirements.txt
"""

# 19. What is Page Factory?
"""
It's a design pattern using `@FindBy` annotation in Java. Python equivalent uses properties or helper methods.
"""

# 20. Integration with Pytest/TestNG?
"""
Use fixtures, parametrize, and setup/teardown methods for test control and data-driven testing.
"""

# 21. How to handle alerts?
""""```python
alert = driver.switch_to.alert
alert.accept()
```"""

# 22. Switch between frames/windows?
"""```python
driver.switch_to.frame('frameName')
driver.switch_to.window(driver.window_handles[1])
```"""

# 23. Handle non-interactable elements?
"""
- Scroll into view using JS
- Wait until visible/clickable
- Use Actions or JS click
"""

# 24. File upload?
"""```python
driver.find_element(By.ID, 'file').send_keys('/path/to/file')
```"""

# 25. Screenshot?
"""```python
driver.save_screenshot('screenshot.png')
```"""

# 26. Reporting?
# Use Allure, HTMLTestRunner, or Pytest-html plugins.

# 27. Headless mode?
"""
```python
options.add_argument('--headless')
```"""

# 28. Run tests in parallel?
"""
Use Selenium Grid or pytest-xdist:
```bash
pytest -n 4
```

"""
# 29. What is Selenium Grid?
# Used to execute tests in parallel across multiple nodes/browsers.

# 30. Handle dynamic web elements?
# Use dynamic XPath, partial text matches, or wait for visibility.

# 31. CI/CD integration?
# Use Jenkins, GitHub Actions, or GitLab CI to run Selenium tests on code push.

# 32. Docker/cloud test execution?
# Use Selenium Docker images or cloud providers like BrowserStack or Sauce Labs.

# 33. Debugging unresponsive click?
# Check for overlays, element state, or JS errors. Use `JavaScriptExecutor` as fallback.

# 34. Random test failures?
# Stabilize with proper waits, isolate flaky data/dependencies.

# 35. Element not clickable?
# May be covered by another element, not in view, or not enabled.

# 36. close() vs quit()?
"""- close(): Closes current tab
- quit(): Closes browser and ends session"""

# 37. StaleElementReferenceException?
# Occurs when element is removed/reloaded. Re-locate the element.

# 38. CAPTCHA handling?
# Not directly possible with Selenium. Needs manual bypass or third-party API.

# 39. Can Selenium handle desktop/mobile apps?
"""No. Use Appium or other tools for that.

# 40. Alternatives to Selenium?
- Playwright
- Cypress
- Puppeteer
- TestCafe"""

# ===========================================================================================

# selenium_robotframework_questions_with_answers.py

"""
Selenium & Robot Framework Interview Questions and Answers
"""

# Existing Selenium content retained...

# --- Robot Framework Interview Questions and Answers ---

# 1. What is Robot Framework?
"""
Robot Framework is an open-source test automation framework for acceptance testing and acceptance test-driven development (ATDD). It uses keyword-driven testing and supports external libraries.
"""

# 2. What are the features of Robot Framework?
"""
- Keyword-driven
- Tabular test data syntax
- Easy integration with SeleniumLibrary, AppiumLibrary, and more
- Data-driven testing
- Reports and logs generation
"""

# 3. How to install Robot Framework?
"""```bash
pip install robotframework
pip install robotframework-seleniumlibrary
```"""

# 4. How to create a test case in Robot Framework?
"""```robot
*** Test Cases ***
Login Test
    Open Browser    https://example.com    chrome
    Input Text      username_field         myuser
    Input Text      password_field         mypass
    Click Button    login_button
    Page Should Contain    Welcome
```"""

# 5. What is a test suite in Robot Framework?
"""
A test suite is a collection of test cases saved in one or more files.
"""

# 6. How to run Robot Framework test cases?
"""```bash
robot test_suite.robot
```

# 7. How to use variables?
```robot
${URL}    https://example.com
```"""

# 8. How to create user-defined keywords?
"""```robot
*** Keywords ***
Login To Application
    Input Text      username_field    myuser
    Input Text      password_field    mypass
    Click Button    login_button
```"""

# 9. How to use setup and teardown?
"""```robot
*** Settings ***
Suite Setup     Open Browser To Login Page
Suite Teardown  Close Browser
```"""

# 10. What are resource files?
"""
Files containing keywords, variables, and other reusable components which can be imported using `Resource` keyword.
"""

# 11. How to import SeleniumLibrary?
"""```robot
*** Settings ***
Library     SeleniumLibrary
```
"""
# 12. What is the difference between `Run Keyword If` and `Run Keywords`?
"""
- `Run Keyword If` is conditional execution
- `Run Keywords` allows multiple keyword execution sequentially
"""

# 13. How to create loops?
"""```robot
:FOR    ${item}    IN    @{list}
\    Log    ${item}
```
"""
# 14. How to handle dropdowns?
"""```robot
Select From List By Value    locator    value
```"""

# 15. How to take screenshots?
"""```robot
Capture Page Screenshot
```"""

# 16. How to pass arguments to a keyword?
"""```robot
*** Keywords ***
Login With Credentials
    [Arguments]    ${username}    ${password}
    Input Text     user_field    ${username}
    Input Text     pass_field    ${password}
```"""

# 17. Reporting in Robot Framework?
"""
Generates output.xml, report.html, and log.html by default.
"""

# 18. How to run tests with tags?
"""```bash
robot -i smoke test_suite.robot
```
"""
# 19. How to integrate Robot Framework with Jenkins?
"""
Use the Robot Framework plugin to publish logs and reports.
"""

# 20. How to use conditions?
"""
```robot
Run Keyword If    '${status}' == 'PASS'    Log    Success
```
"""

# 21. Can we use Robot Framework for API Testing?
"""
Yes, using libraries like `RequestsLibrary`.
"""

# 22. Parallel execution in Robot Framework?
"""
Use `pabot`:
```bash
pabot --processes 4 test_suite.robot
```
"""

# 23. Debugging in Robot Framework?
"""
Use `Log`, `Log To Console`, and `BuiltIn` library for debugging purposes.
"""

# 24. How to handle dynamic locators?
"""
Use XPath with variables or parameterized locators.
"""

# 25. How to use environment variables?
"""
```robot
${ENV} =    Get Environment Variable    VAR_NAME
```
"""

# 26. Differences between Selenium and Robot Framework?
"""
Selenium is a web automation tool, Robot Framework is a test automation framework that can use Selenium as a library.
"""

# 27. What are listeners in Robot Framework?
"""
Listeners are Python classes that can receive notifications during test execution.
"""

# 28. Can you call Python scripts from Robot Framework?
"""
Yes, using `Process` or writing custom Python keywords.
"""

# 29. Robot Framework limitations?
"""
- Not suitable for unit testing
- Slower than code-based frameworks for complex logic
- Debugging can be verbose
"""

# 30. Tools supporting Robot Framework?
"""
- RIDE (IDE for Robot)
- VS Code with Robot Framework extension
- Jenkins
- Browser library (for web automation)
"""
