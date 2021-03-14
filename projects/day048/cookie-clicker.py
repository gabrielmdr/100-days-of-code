from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time

# The path to your Selenium Web Driver for Google Chrome. Download at https://chromedriver.chromium.org/downloads
chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

five_min = time.time() + 5 * 60
timeout = time.time() + 5

while True:
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)

    cookie = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions) \
        .until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#bigCookie")))
    try:
        cookie.click()
    except ElementClickInterceptedException:
        pass

    cookies = driver.find_element_by_id("cookies") or None
    if cookies:
        try:
            amount = int(cookies.text.split(" ")[0])
        except ValueError:
            amount = 0
        if time.time() > timeout:
            products = driver.find_elements_by_css_selector(".product.unlocked.enabled")
            for i in range(len(products) - 1, -1, -1):
                product_amount = int(products[i].find_element_by_css_selector(".content .price").text)
                if amount >= product_amount:
                    products[i].click()

    if time.time() >= five_min:
        cookies_per_sec = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#cookies"))).text
        cps_value = cookies_per_sec.splitlines()[1].split(":")[1].strip()
        print(f"{cps_value} cookies per second")
        break

driver.quit()
