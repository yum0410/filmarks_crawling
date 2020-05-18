from selenium import webdriver
import os
import sys
import pandas as pd
from tqdm import tqdm
import time


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="./chromedriver")

    driver.get("https://filmarks.com/login")

    driver.find_elements_by_link_text('Facebookで登録・ログイン')[0].click()

    driver.find_element_by_name('email').send_keys("XXXXX@gmail.com")
    driver.find_element_by_name('pass').send_keys("XXXXX")
    driver.find_element_by_id('loginbutton').click()
    driver.get("https://filmarks.com/list/vod")

    time.sleep(10)
    # 下スクロール => フッタークリック
    driver.find_elements_by_link_text('動画配信サービスで探す')[0].location_once_scrolled_into_view
    driver.find_elements_by_link_text('動画配信サービスで探す')[0].click()
    driver.find_elements_by_link_text('Amazon Prime Videoで鑑賞できる映画')[0].click()

    # クローリング
    time.sleep(10)
    movies = driver.find_elements_by_class_name("js-movie-cassette")
    movies_info = []
    for movie in movies:
        movie_info = {}
        import ipdb; ipdb.set_trace()
        movie_info["title"] = movie.find_elements_by_class_name("p-content-cassette__title")[0].text
        genres = movie.find_elements_by_class_name("p-content-cassette__genre")[0].find_elements_by_tag_name("li")
        movie_info["genre"] = [g.text for g in genres]
        movie_info["rate"] = movie.find_element_by_class_name("c-rating__score").text
        movies_info.append(movie_info)
