import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def save_to_file(file_name, rows):
    with open(file_name, 'a+', newline='', encoding="utf-8") as write_obj:
        for row in rows:
            write_obj.write(row.attrs['href']+"\n")


def get_news_links(urls_list, driver, key_words):
    for url in urls_list:

        driver.get(url[0].lower())
        time.sleep(5)

        print(url[0])
        for word in key_words:
            search_query = driver.find_element_by_name(url[2])
            search_query.clear()
            search_query.send_keys(word)

            search_query.send_keys(Keys.RETURN)
            if url[1].split(',')[0] == 'class':
                try:
                    time.sleep(5)
                    content = driver.page_source
                    soup = BeautifulSoup(content, features="lxml")
                    news_links = soup.findAll('a', attrs={'class', url[1].split(',')[1]})

                    # price_tag=driver.find_element_by_class_name(url[1].split(',')[1]).text.strip()
                    print(word + ", " +str(news_links))
                    save_to_file(word+".txt", news_links)
                except:
                    print(word)
            elif url[1].split(',')[0] == 'id':
                try:
                    time.sleep(5)
                    price_tag=driver.find_elements_by_xpath("//*[contains(@id, '"+url[1].split(',')[1]+"')]")[0].text.strip()
                    print(word + ", " +price_tag)
                except:
                    print(word)
            elif url[1].split(',')[0] == 'color':
                try:
                    time.sleep(30)
                    content = driver.page_source
                    soup = BeautifulSoup(content, features="lxml")
                    price_tag = soup.findAll('font', attrs={'color':url[1].split(',')[1]})[0].contents[0].contents[0].strip()
                    print(word + ", " + price_tag)
                except:
                    print(word)


if __name__ == '__main__':
    # url of state to scrap data from...
    urls_list = [['https://www.dawn.com/search', 'class,gs-title', 'q'],
                 ['https://www.bbc.co.uk/search?q=', "class,ssrcss-vh7bxp-PromoLink", 'q']]

    key_words = ['blackout']

    driver = webdriver.Firefox(executable_path="geckodriver")

    geners = get_news_links(urls_list, driver, key_words)

    driver.quit()
