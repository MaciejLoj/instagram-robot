from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import random

class InstaRobot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_link_text('Log in')
        login_button.click()
        time.sleep(2)
        username_field = driver.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(2)
        password_field = driver.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        second_login = driver.find_element_by_css_selector('button.L3NKy')
        second_login.click()
        time.sleep(5)

    def find_photos(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)
        sum_of_pics = []
        for i in range(3): # range(1) = 51 photos, range(2) = 51 + 24 = 75 photos, range(3) = 51 + 24 + 24 = 99 photos, etc
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            a_tags = driver.find_elements_by_tag_name('a')
            photos_hrefs = [photo.get_attribute('href') for photo in a_tags]
            photos_hrefs = [href for href in photos_hrefs if '/p/' in href]
            for photo_href in photos_hrefs:
                if photo_href not in sum_of_pics:
                    sum_of_pics.append(photo_href)
            print(len(sum_of_pics))
        for pic in sum_of_pics:
            driver.get(pic)
            try: # If you want to block some of options just use hashtag before line of code
                time.sleep(4)
                driver.find_element_by_css_selector('button.coreSpriteHeartOpen').click() # LIKE PHOTO
                time.sleep(4)
                driver.find_element_by_css_selector('textarea.Ypffh').click() # COMMENT ON PHOTO
                time.sleep(10)
                list_of_comments = ['😊', ';)', '🙂🌸', ':))', '🌸🤗'] #use whatever you like, but use many different
                a = random.choice(list_of_comments)
                driver.find_element_by_css_selector('textarea.Ypffh').send_keys(a)
                time.sleep(10)
                driver.find_element_by_css_selector('textarea.Ypffh').send_keys(Keys.RETURN)
                time.sleep(2)
                driver.find_element_by_css_selector('button.oW_lN').click()  # FOLLOW OWNER
                time.sleep(10)
            except Exception as e:
                time.sleep(12)

    def my_followers(self):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self.username + "/")
        amount_my_followers = int(driver.find_element_by_xpath("//li[2]/a/span").text)
        print(amount_my_followers)
        window_followers = driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[2]/a')
        window_followers.click()
        time.sleep(2)
        global all_followers
        all_followers = []
        for i in range(int(amount_my_followers/4)):
            visible_followers = driver.find_elements_by_class_name("FPmhX")
            for element in visible_followers:
                title = element.get_property('title')
                if title not in all_followers:
                    all_followers.append(title)
            for _ in range(5):
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        print(all_followers)


    def am_following(self):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self.username + "/")
        amount_my_followings = driver.find_element_by_xpath('//li[3]/a/span').text
        amount_my_followings = float(amount_my_followings.replace(',',''))
        print(amount_my_followings)
        window_followings = driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a')
        window_followings.click()
        time.sleep(2)
        global all_followings
        all_followings = []
        for i in range(int(amount_my_followings/4)):
            visible_followings = driver.find_elements_by_class_name("FPmhX")
            for element in visible_followings:
                title = element.get_property('title')
                if title not in all_followings:
                    all_followings.append(title)
            for _ in range(5):
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        print(all_followings)


    def accounts_to_unfollow(self):
        dictionary_to_unfollow = {}
        for account in all_followings:
            account_index = all_followings.index(account)
            account_index += 1
            dictionary_to_unfollow[account] = account_index
            if account in all_followers:
                dictionary_to_unfollow.pop(account)
        print(dictionary_to_unfollow)
        driver = self.driver
        driver.get("https://www.instagram.com/" + self.username + "/")
        amount_my_followings = driver.find_element_by_xpath('//li[3]/a/span').text
        amount_my_followings = float(amount_my_followings.replace(',',''))
        window_followings = driver.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a')
        window_followings.click()
        for _ in range(int(amount_my_followings)):
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        visible_followings = driver.find_elements_by_class_name("FPmhX")
        for element in visible_followings:
            title = element.get_property('title')
            if title in dictionary_to_unfollow:
                time.sleep(2)
                driver.find_element_by_xpath(('/html/body/div[3]/div/div/div[2]/ul/div/li['
                                             + str(dictionary_to_unfollow[title])+']/div/div[2]/button')).click()
                time.sleep(3)
                driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
                time.sleep(3)


user1 = InstaRobot("your_instagram_login", "your_instagram_password")
user1.login()
user1.find_photos('hashtag')  # type whatever you like, apple, car, etc
user1.my_followers()
user1.am_following()
user1.accounts_to_unfollow()

