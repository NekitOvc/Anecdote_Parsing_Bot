from bs4 import BeautifulSoup

import requests
import random
import logging

# логирование в файл py_log.log в режиме перезаписи при каждом запуске бота с указанием времени
logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')

URL = 'https://www.anekdot.ru/last/anekdot' #url, с которым будем работать

class ParserURL:
    def parser_url(url):
        r = requests.get(url) #отправляем get-запрос
        logging.info(f'Статус подключения: {r.status_code}') #проверка подключения

        soup = BeautifulSoup(r.text, 'html.parser')
        anekdots = soup.find_all('div', class_='text') #поиск тега div с классом text
        return [c.text for c in anekdots] #из anekdots выбирается только текст

    list_of_jokes = parser_url(URL) #итоговый список анекдотов
    random.shuffle(list_of_jokes) #перемешанный список
