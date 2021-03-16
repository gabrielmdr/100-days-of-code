from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "Your e-mail address registered in LinkedIn"
ACCOUNT_PASSWORD = "Your LinkedIn password"
PHONE = "Your phone number"

# The path to your Selenium Web Driver for Google Chrome. Download at https://chromedriver.chromium.org/downloads
chrome_driver_path = "C:\\Development\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("Your LinkedIn job search link")

time.sleep(2)
# "Entrar" in pt-BR. Replace for "Sign in" in en-US or the corresponding word in your language
sign_in_button = driver.find_element_by_link_text("Entrar")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        save_button = driver.find_element_by_css_selector(".jobs-save-button")
        # "Salvar" in pt-BR. Replace for "Save" in en-US or the corresponding word in your language
        if save_button.find_element_by_css_selector("span").text == "Salvar":
            save_button.click()
            print("Saved\n")
        time.sleep(5)

    except NoSuchElementException:
        print("No save button, skipped.\n")
        continue

time.sleep(5)
driver.quit()
