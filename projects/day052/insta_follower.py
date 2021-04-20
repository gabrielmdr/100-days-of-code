from selenium import webdriver

import time

# The path to your Selenium Web Driver for Google Chrome. Download at https://chromedriver.chromium.org/downloads
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
SIMILAR_ACCOUNT = "instagram"
USERNAME = "Your username"
PASSWORD = "Your password"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        return

    def login(self):
        self.driver.get("https://instagram.com")

        time.sleep(10)

        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_css_selector("button[type=submit]")

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        submit_button.click()

        time.sleep(5)
        return

    def find_followers(self):
        self.driver.get(f"https://instagram.com/{SIMILAR_ACCOUNT}")

        followerslist_button = self.driver.find_element_by_css_selector("a.-nal3")
        followerslist_button.click()

        time.sleep(3)
        return

    def follow(self):
        followerslistcontainer_div = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        followerslist_ul = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
        followers_li = followerslist_ul.find_elements_by_tag_name("li")

        while len(followers_li) < 250:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight + 300", followerslistcontainer_div)
            followers_li = followerslist_ul.find_elements_by_tag_name("li")

        for i in range(250):
            follow_button = followers_li[i].find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")

            if follow_button.text == "Follow":
                follow_button.click()
                time.sleep(1)
        return

    def close(self):
        self.driver.close()
        return
