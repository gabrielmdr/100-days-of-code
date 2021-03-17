from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

import time

# The path to your Selenium Web Driver for Google Chrome. Download at https://chromedriver.chromium.org/downloads
chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

base_window = driver.window_handles[0]

time.sleep(5)
signin_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button")
signin_button.click()

time.sleep(5)
login_with_fb_button = driver.find_element_by_xpath("//*[@id='t--1610880557']/div/div/div[1]/div/div[3]/span/div[2]/button")
login_with_fb_button.click()

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

time.sleep(5)
fb_email_input = driver.find_element_by_xpath("//*[@id='email']")
fb_email_input.send_keys("Your Facebook e-mail address")
fb_email_input = driver.find_element_by_xpath("//*[@id='pass']")
fb_email_input.send_keys("Your Facebook password")
fb_login_button = driver.find_element_by_css_selector("input[type='submit']")
fb_login_button.click()

driver.switch_to.window(base_window)

try:
    time.sleep(5)
    allow_location_button = driver.find_element_by_xpath("//*[@id='t--1610880557']/div/div/div/div/div[3]/button[1]")
    allow_location_button.click()
except NoSuchElementException:
    print("No 'Allow location button'.")

try:
    time.sleep(2)
    disallow_notifications_button = driver.find_element_by_xpath("//*[@id='t--1610880557']/div/div/div/div/div[3]/button[2]")
    disallow_notifications_button.click()
except NoSuchElementException:
    print("No 'Disallow notifications button'.")

try:
    time.sleep(2)
    allow_cookies_button = driver.find_element_by_xpath("//*[@id='t-429325247']/div/div[2]/div/div/div[1]/button")
    allow_cookies_button.click()
except NoSuchElementException:
    print("No 'Allow cookies button'.")

time.sleep(5)
for i in range(10):
    time.sleep(1)
    try:
        yes_button = driver.find_element_by_xpath("//*[@id='t-429325247']/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button")
        yes_button.click()
    except NoSuchElementException:
        print("No dislike button yet.")
        time.sleep(2)
        try:
            yes_button = driver.find_element_by_xpath("//*[@id='t-429325247']/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button")
            yes_button.click()
        except NoSuchElementException:
            print("No dislike button. Passing")
    except ElementClickInterceptedException:
        dismiss_add_to_home_button = driver.find_element_by_xpath("//*[@id='t--1610880557']/div/div/div[2]/button[2]")
        dismiss_add_to_home_button.click()

driver.quit()
