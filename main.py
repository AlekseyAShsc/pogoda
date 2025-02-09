import logging
# import os.path
# import re
# import time
import datetime
# import random
from loader_url import reader_url_saved_text
from weathe_sampling import sampling_month

logging.basicConfig(
    filename="pogoda.log",
    # format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s',
    format= '%(levelname)-8s [%(asctime)s] - %(filename)-25s:'\
           '%(lineno)d - %(name)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)


if __name__ == '__main__':

    # month_select = {
    #     "january", "Январь";
    #     "february", "Февраль";
    #     "march", "Март";
    #     "april", "Апрель";
    #     "may", "Май";
    #     "june", "Июнь";
    #     "july", "Июль";
    #     "august", "Август";
    #     "september", "Сентябрь";
    #     "october", "Октябрь";
    #     "november", "Ноябрь";
    #     "december", "Декабрь";
    # }
    year_cet = ["2020", "2021", "2022", "2023", "2024"]
    month_cet = ["january", "february", "march", "april", "may", "june", "july", "august", "september",  "october",  "november", "december"]
    
    nacalo = datetime.datetime.now()  # время
    sleep_sum = 0  # сумарное время простоя
    kolvo = 0
    for year_select in year_cet:
        for month_select in month_cet:
            data_url = f'{month_select}-{year_select}'
            reader_url_saved_text(data_url)
            sampling_month()
    konec = datetime.datetime.now()
    print(f'{konec} - {nacalo} = {konec-nacalo}')
    logger.info(f"{konec} - {nacalo} = {konec-nacalo}. Готово!")
    print("Готово")