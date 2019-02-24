""" Importing necessary tools """

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

import random


""" Creating InstaRobot class with its methods allowing us to choose from many options that the bot will use """

class InstaRobot:

    """ 'Creator' with its parameters: username, password. Everytime you create an instance you have to put them """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    """ Method closing our browser"""
    def close_browser(self):
        self.driver.close()

    """ Method allowing us to log into our account. You can change the time.sleep() to wait longer/shorter """
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

    """ Method finding photos by given hashtag (parameter) you have to put. Type in whatever you like """
    def find_photos(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)
        sum_of_pics = []
        """ range(1) = 51 photos, range(2) = 51 + 24 = 75 photos, range(3) = 51 + 24 + 24 = 99 photos, etc """
        for i in range(3):
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
            try:
                """ If you want to block some of options just use hashtag before line of code """
                time.sleep(4)
                driver.find_element_by_css_selector('button.coreSpriteHeartOpen').click() # LIKING PHOTO
                time.sleep(4)
                driver.find_element_by_css_selector('textarea.Ypffh').click() # COMMENTING ON PHOTO
                time.sleep(10)
                list_of_comments = ['😊', ';)', '🙂🌸', ':))', '🌸🤗'] #use whatever you like, but use many different
                a = random.choice(list_of_comments)
                driver.find_element_by_css_selector('textarea.Ypffh').send_keys(a)
                time.sleep(10)
                driver.find_element_by_css_selector('textarea.Ypffh').send_keys(Keys.RETURN)
                time.sleep(2)
                driver.find_element_by_css_selector('button.oW_lN').click()  # FOLLOWING PIC OWNER
                time.sleep(10)
            except Exception as e:
                time.sleep(12)

    """ Method creating a list with our followers. Then it will be used to compare with our list of followings and 
    create a list with those who does not follow us"""
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
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        print(all_followers)

    """ Method creating a list with our followings. Then it will be used to compare with our previous list - list 
    of our followers and will create a list of those who does not follow us"""
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
                driver.find_element_by_xpath('/html/body/div[2]/div/div[2]').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        print(all_followings)

    """ Method comparing previous lists and creating dictionary with accounts that we follow but they do not follow us.
    Additionally there is an index for each photo created based on followings list. 
    It will be used to unfollow such an account."""
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
            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]').send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        visible_followings = driver.find_elements_by_class_name("FPmhX")
        for element in visible_followings:
            title = element.get_property('title')
            if title in dictionary_to_unfollow:
                time.sleep(2)
                driver.find_element_by_xpath(('/html/body/div[2]/div/div[2]/ul/div/li['+str(dictionary_to_unfollow[title])+']/div/div[3]/button')).click()
                time.sleep(3)
                driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[1]').click()
                time.sleep(3)


""" Creating instance of a InstaRobot class. You have to type in your credentials """

user1 = InstaRobot("your_login", "your_password")

"""Using class methods to initate the bot"""

user1.login()
user1.find_photos('give_your_hashtag')
user1.my_followers()
user1.am_following()
user1.accounts_to_unfollow()

