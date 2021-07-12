# Парсим https://dubaigold.ru/mens-chain. 
from bs4 import BeautifulSoup
import requests

response = requests.get('https://dubaigold.ru/mens-chain')
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html5lib")
    item_list = soup.find_all('div', {'class': 'name'})    # собираем все теги с ссылками на страницы товаров

    Links = []
    for item in item_list:    # создаем массив ссылок на товары страницы
        l = item.a
        l1 = l.get('href')    # функцию get по вытаскиванию из тегов url подсказали на https://habr.com/ru/sandbox/151294/
        Links.append(l1)

    # собираем и выводим характеристики товаров
    for ani in Links:
        response1 = requests.get(ani)
        if response1.status_code == 200:
            soup1 = BeautifulSoup(response1.text, features="html5lib")
            name = soup1.find('h1')
            print(name.text)    # название товара
            price = soup1.find('div', class_ ='price-product')
            s = price.text
            print(s.strip())    # цена товара
            item_description = soup1.find('tbody')
            rows = item_description.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                count = 0
                for col in cols:
                    if count == 0:
                        named = col.text
                    elif count == 1:
                        descr = col.text
                    count += 1
                print(named, ":", descr)
            print()
