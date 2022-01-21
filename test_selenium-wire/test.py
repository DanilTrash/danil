from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver  # Import from seleniumwire


driver = webdriver.Chrome()
driver.get('https://www.instagram.com')
element = WebDriverWait(driver, 10).until(lambda d: driver.find_element(By.XPATH, '//input[@name="username"]'))
element.send_keys('daniella_svveet')
element = WebDriverWait(driver, 10).until(lambda d: driver.find_element(By.XPATH, '//input[@name="password"]'))
element.send_keys('Zxcasdqwe123')
element = WebDriverWait(driver, 10).until(lambda d: driver.find_element(By.XPATH, '//button/div'))
element.click()


for request in driver.requests:
    print(request.params)
