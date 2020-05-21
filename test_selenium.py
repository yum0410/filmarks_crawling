from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import sys
import pandas as pd
from tqdm import tqdm
import time


def get_movie_elements(movie):
    movie_info = {}
    class_names = [x.get_attribute("class") for x in movie.find_element_by_class_name("p-content-cassette__info__main").find_elements_by_tag_name("div")]
    for class_name in class_names:
        if class_name == "p-content-cassette__action__body":
            movie_info["watched"] = movie.find_elements_by_class_name(class_name)[0].text
            movie_info["see_later"] = movie.find_elements_by_class_name(class_name)[1].text
        elif class_name == "p-content-cassette__title-wrapper":
            title_info = movie.find_element_by_class_name(class_name)
            movie_info["title"] = title_info.find_element_by_class_name("p-content-cassette__title").text
            movie_info["how_to_see"] = title_info.find_element_by_class_name("c-vod-service-types__horizontal").text.split("\n")
        elif class_name == "p-content-cassette__other-info":
            outer_info = movie.find_element_by_class_name(class_name)
            for info in outer_info.find_elements_by_class_name("p-content-cassette__other-info__title"):
                if info.text == "上映日：":
                    movie_info["release_date"] = movie.find_element_by_class_name("p-content-cassette__other-info").find_elements_by_tag_name("span")[0].text
                elif info.text == "製作国：":
                    countrys = movie.find_element_by_class_name("p-content-cassette__other-info").find_elements_by_tag_name("a")
                    movie_info["country"] = [c.text for c in countrys]
                elif info.text == "上映時間：":
                    movie_info["show_time"] = movie.find_element_by_class_name("p-content-cassette__other-info").find_elements_by_tag_name("span")[-1].text
        elif class_name == "p-content-cassette__genre":
            genres = movie.find_elements_by_class_name(class_name)[0].find_elements_by_tag_name("li")
            movie_info["genre"] = [g.text for g in genres]
        elif class_name == "c-rating__score":
            movie_info["rate"] = movie.find_element_by_class_name(class_name).text
        elif class_name == "p-content-cassette__synopsis-desc__text":
            movie_info["synopsis"] = movie.find_element_by_class_name(class_name).text
        elif class_name == "p-content-cassette__people":
            casts = movie.find_elements_by_class_name(class_name)
            for cast in casts:
                for c in cast.find_elements_by_class_name("p-content-cassette__people-wrap"):
                    cast_type = c.find_element_by_class_name("p-content-cassette__people-list-term").text
                    if cast_type == "監督":
                        movie_info["directer"] = [name.text for name in c.find_elements_by_tag_name("ul")]
                    elif cast_type == "脚本":
                        movie_info["writer"] = [name.text for name in c.find_elements_by_tag_name("ul")]
                    elif cast_type == "出演者":
                        movie_info["actor"] = [name.text for name in c.find_elements_by_tag_name("ul")]
    movie_info["best_reviews"] = [x.text for x in movie.find_elements_by_class_name("p-content-cassette__review__text")]
    return movie_info


def get_movies_info(crawling_page_num=1):
    movies_info = []
    for i in tqdm(range(1, crawling_page_num + 1)):
        driver.get("https://filmarks.com/list/vod/amazon_video?page={}".format(i))
        movies = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'p-contents-grid'))
        ).find_elements_by_class_name("js-movie-cassette")
        for movie in tqdm(movies):
            movies_info.append(get_movie_elements(movie))
    return movies_info


def crawling(crawling_page_num=5 , retry_num=3):
    i = 0
    while i < retry_num:
        try:
            movies_info = get_movies_info(crawling_page_num)
        except Exception as e:
            i = i + 1
            print("ERROR", e)
            continue
        else:
            return movies_info


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get("https://filmarks.com/login")
    driver.find_elements_by_link_text('Facebookで登録・ログイン')[0].click()

    driver.find_element_by_name('email').send_keys("XXXXX@gmail.com")
    driver.find_element_by_name('pass').send_keys("XXXXX")
    driver.find_element_by_id('loginbutton').click()
    time.sleep(1)

    driver.get("https://filmarks.com/list/vod")
    element = WebDriverWait(driver, 10).until(
	    EC.visibility_of_element_located((By.LINK_TEXT, 'Amazon Prime Videoで鑑賞できる映画'))
    ).click()
    movies_info = crawling(5)
    movies_info = pd.DataFrame(movies_info)
    movies_info.to_csv("./movies_info.csv", encoding="utf-8-sig")
        # TODO #1 続きを見る　の先もクローリング
