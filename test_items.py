import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestMainPage():
    def test_adding_item_to_bin(self, browser):
        browser.get(link)
        browser.implicitly_wait(10)
        add_to_bin_buttons = browser.find_elements(By.XPATH, "//div[contains(@class,'product_main')]//button[@type='submit']")
        time.sleep(5)
        assert len(add_to_bin_buttons) > 0, 'button not found'
