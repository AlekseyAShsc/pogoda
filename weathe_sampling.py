import logging
from bs4 import BeautifulSoup


logging.basicConfig(
    filename="pogoda.log",
    # format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s',
    format= '%(levelname)-8s [%(asctime)s] - %(filename)-25s:'\
        '%(lineno)d - %(name)s - %(message)s',
    level=logging.DEBUG,
    filemode="w"
)

logger = logging.getLogger(__name__)

month_select = {
    "01": "Январь",
    "02": "Февраль",
    "03": "Март",
    "04": "Апрель",
    "05": "Май",
    "06": "Июнь",
    "07": "Июль",
    "08": "Август",
    "09": "Сентябрь",
    "10": "Октябрь",
    "11": "Ноябрь",
    "12": "Декабрь",
}


# Чтение из файла и преобразовываем с soup return BeautifulSoup
def read_text():
    try:
        with open("index.html", "r", encoding="utf-8") as w_file:
            src = w_file.read()
        return BeautifulSoup(src, "lxml")
    except Exception as err:
        logging.error(f"Ошибка чтения из файла. Ошибка {err}")


def sampling_month():
    bs = read_text()
    logging.info(f"Разбираем bs, {type(bs)}")
    month_period = bs.find_all('a', class_='calendar-item')
    logging.info(f"month_period = {type(bs)}")
    for days in month_period:
        # logging.info(days)
        # logging.info(type(days))
        if not days.find('span', class_='no-data'):
            # Вариант 1
            #calendar_day = (days.find('span', class_='month-calendar-day')).string
            calendar_month = (days['href']).split('/')[2]
            calendar_month_chareds = int(calendar_month.split('-')[1])
            calendar_day_chareds = int(calendar_month.split('-')[0])
            # blok.find('a').get('href')
            # calendar_temp = days.find('span', class_='month-calendar-temp').find_all('span').string
            calendar_temp = days.find('span', class_='month-calendar-temp').text.replace(' ', '').split('\n')[:2]
            calendar_temp_morning = calendar_temp[0]
            calendar_temp_evening = calendar_temp[1]
            # calendar_temp_2 = calendar_temp.find('span').text
            # for day_tamp in calendar_temp.find_all('span'):
            #     logging.info(f"day_tamp.string = {day_tamp.string}")
            logging.info(f"{calendar_day_chareds} : {calendar_month_chareds} - Утром = {calendar_temp_morning}. Вечером = {calendar_temp_evening}")
            # Вариант 2
            # logging.info(f"days.find_all('span') = {days.find_all('span')}")




if __name__ == '__main__':
    # pass
    sampling_month()
