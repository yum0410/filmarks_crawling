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

    driver.implicitly_wait(5)
    # 下スクロール => フッタークリック
    driver.find_elements_by_link_text('動画配信サービスで探す')[0].location_once_scrolled_into_view
    driver.find_elements_by_link_text('動画配信サービスで探す')[0].click()
    driver.find_elements_by_link_text('Amazon Prime Videoで鑑賞できる映画')[0].click()

    # TODO #2 ページ読み込みが完了するまでプロセスを停止させる ※driver.implicitly_wait(120)では止まらない
    driver.implicitly_wait(120)
    movies_info = []
    try:
        movies = driver.find_elements_by_class_name("js-movie-cassette")
        for movie in movies:
            movie_info = {}
            movie_info["watched"] = movie.find_elements_by_class_name("p-content-cassette__action__body")[0].text
            movie_info["see_later"] = movie.find_elements_by_class_name("p-content-cassette__action__body")[1].text

            movie_info["title"] = movie.find_elements_by_class_name("p-content-cassette__title")[0].text
            movie_info["release_date"] = movie.find_element_by_class_name("p-content-cassette__other-info").find_elements_by_tag_name("span")[0].text
            movie_info["country"] = movie.find_element_by_class_name("p-content-cassette__other-info").find_element_by_tag_name("a").text
            movie_info["show_time"] = movie.find_element_by_class_name("p-content-cassette__other-info").find_elements_by_tag_name("span")[1].text
            genres = movie.find_elements_by_class_name("p-content-cassette__genre")[0].find_elements_by_tag_name("li")
            movie_info["genre"] = [g.text for g in genres]
            movie_info["rate"] = movie.find_element_by_class_name("c-rating__score").text
            movie_info["synopsis"] = movie.find_element_by_class_name("p-content-cassette__synopsis-desc__text").text
            movie_info["directer"] = movie.find_elements_by_class_name("c-label")[0].text
            movie_info["writer"] = movie.find_elements_by_class_name("c-label")[1].text
            movie_info["actor"] = [x.text for x in movie.find_elements_by_class_name("p-content-cassette__people-list-desc")[2:]]

            movie_info["how_to_see"] = [x.text for x in movie.find_elements_by_class_name("c-vod-service-types__horizontal")]
            movie_info["best_reviews"] = [x.text for x in movie.find_elements_by_class_name("p-content-cassette__review__text")]

            movies_info.append(movie_info)
    except Exception as e:
        print("time out!", e)

    print("DONE", movies_info)
        # TODO #1 続きを見る　の先もクローリング
