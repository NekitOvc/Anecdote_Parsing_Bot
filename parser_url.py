from bs4 import BeautifulSoup

import requests
import random
import logging

# логирование в файл py_log.log в режиме перезаписи при каждом запуске бота с указанием времени
logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')

# url, с которым будем работать
URL = 'https://www.anekdot.ru/last/anekdot' 

def parser(url):
    # отправляем get-запрос
    r = requests.get(url)
    # проверка подключения
    logging.info(f'Статус подключения: {r.status_code}')

    soup = BeautifulSoup(r.text, 'html.parser')
    # поиск тега div с классом text
    anekdots = soup.find_all('div', class_='text')
    # из anekdots выбирается только текст
    return [c.text for c in anekdots]

# итоговый список анекдотов
list_of_jokes = parser(URL)
# перемешанный список
random.shuffle(list_of_jokes)