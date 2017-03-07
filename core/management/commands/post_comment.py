# -*- coding: utf-8 -*-
import time
import datetime
from django.core.management.base import BaseCommand
from selenium import webdriver
import os

from core.models import Post

chromedriver = "/home/andrey/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
driver.set_window_size(1600,1200)


class Command(BaseCommand):
    help = "Describe the Command Here"

    def open_driver(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chromeOptions.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
        driver.set_window_size(1600, 1200)

    def handle(self, **options):
        posts = Post.objects.filter(is_published=False).filter(
            publication_date__gte=datetime.datetime.now() - datetime.timedelta(minutes=30)).select_related('account').order_by('publication_date')
        for post in posts:
            account = post.account
            comment = post.comment
            link = post.link
            password = account.password
            email = account.name
            self.login(email, password)
            time.sleep(5)
            self.post_comment(link, comment)
            time.sleep(5)
            driver.close()
            self.open_driver()

    def post_comment(self, link, comment):
        from selenium.webdriver.common.keys import Keys
        driver.get(link)
        time.sleep(5)
        comment_input = driver.find_element_by_css_selector('.reply_field.submit_post_field')
        comment_input.click()
        comment_input.send_keys(comment)
        comment_input.send_keys(Keys.RETURN)
        time.sleep(1)

    def login(self, email, password):
        driver.get("https://vk.com/login")
        email_input = driver.find_element_by_css_selector('#email')
        password_input = driver.find_element_by_css_selector('#pass')
        login = driver.find_element_by_css_selector('#login_button')
        email_input.send_keys(email)
        password_input.send_keys(password)
        login.click()
