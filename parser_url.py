import requests
import random
from bs4 import BeautifulSoup
from logger import setup_logging

logger = setup_logging()

URL = "https://www.anekdot.ru/last/anekdot"

def parser(url):
    response = requests.get(url)
    logger.info(f"Статус подключения: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    anekdots = soup.find_all("div", class_="text")
    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)