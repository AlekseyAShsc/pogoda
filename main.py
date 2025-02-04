import logging
import os.path
import requests
from bs4 import BeautifulSoup
import re
import time
import datetime
import random
import json
# from fake_useragent import UserAgent
from loader_url import reader_url_saved_text as rust

logging.basicConfig(
    filename="pogoda.log",
    format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)


if __name__ == '__main__':

    nacalo = datetime.datetime.now()  # время
    sleep_sum = 0  # сумарное время простоя
    kolvo = 0

    data_url = 'january-2024'
    rust(data_url) # Сохраняем страницу со списком машин этого производителя

    konec = datetime.datetime.now()
    print(f'{konec} - {nacalo} = {konec-nacalo}')
    print("Готово")