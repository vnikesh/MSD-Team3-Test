#Author : Deepika
#Final Test Demo

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC003_NurseLogin(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()


   def test_nurse_login(self):
       user = "unmc"
       pwd = "unmc2017"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://durangopy-bed-track.herokuapp.com")
       assert "Logged In"

       # To Navigate to the Login button for Nurse login
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[2]/a")
       elem.click()
       time.sleep(2)

       # Fetch the user ID and password by giving the below codes
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

   def tearDown(self):
       self.driver.close()
