from selenium import webdriver
import os
import sys
import pandas as pd
from tqdm import tqdm


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="./chromedriver")

    driver.get("https://filmarks.com/login")

    driver.find_elements_by_link_text('Facebookで登録・ログイン')[0].click()

    driver.find_element_by_name('email').send_keys("XXXXX@gmail.com")
    driver.find_element_by_name('pass').send_keys("XXXXX")
    driver.find_element_by_id('loginbutton').click()
    driver.get("https://filmarks.com/list/vod")

    driver.find_elements_by_link_text('Amazon Prime Videoで鑑賞できる映画')[0].click()

    import ipdb; ipdb.set_trace()

