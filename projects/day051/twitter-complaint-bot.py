from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time

CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
TWITTER_EMAIL = "Your Twitter account e-mail address"
TWITTER_PASSWORD = "Your Twitter account password"
PROMISED_DOWN = 20
PROMISED_UP = 7.5


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go_button.click()
        time.sleep(60)
        download_span = self.driver.find_element_by_css_selector(".download-speed")
        download_speed = float(download_span.text)
        upload_span = self.driver.find_element_by_css_selector(".upload-speed")
        upload_speed = float(upload_span.text)
        self.down = download_speed
        self.up = upload_speed
        print(f"Download speed: {self.down}")
        print(f"Upload speed: {self.up}")
        return

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.get("https://twitter.com/login")
            time.sleep(10)
            email_input = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
            password_input = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
            email_input.send_keys(TWITTER_EMAIL)
            password_input.send_keys(TWITTER_PASSWORD)
            login_button = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
            login_button.click()
            time.sleep(20)
            tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            try:
                draft_input = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
                draft_input.send_keys(tweet)
                tweet_button = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span")
                tweet_button.click()
            except NoSuchElementException:
                print("Could not tweet.\n")
        time.sleep(5)
        self.driver.quit()
        return
