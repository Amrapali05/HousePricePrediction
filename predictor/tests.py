from django.test import TestCase

from django.test import LiveServerTestCase
from selenium import webdriver


class HomePageTest(LiveServerTestCase):

    def test_home_page(self):
        driver = webdriver.Chrome()

        driver.get(self.live_server_url)

        print("Page Title:", driver.title)

        driver.quit()