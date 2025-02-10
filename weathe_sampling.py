import logging
from bs4 import BeautifulSoup
import pandas as pd


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
    # logging.info(f"Разбираем bs, {type(bs)}")
    month_period = bs.find_all('a', class_='calendar-item')
    # logging.info(f"month_period = {type(bs)}")
    result = []
    for days in month_period:
        if not days.find('span', class_='no-data'):
            try:
                calendar_month = (days['href']).split('/')[2]
                calendar_month_chareds = int(calendar_month.split('-')[1])
            except:
                calendar_month = "нет данных"
                calendar_month_chareds = "нет данных"
                logging.error(f"Нет месяца. {days}")
            try:
                calendar_day_chareds = int(calendar_month.split('-')[0])
            except:
                calendar_day_chareds = "нет данных"
                logging.error(f"Нет дня. {days}")
            try:
                calendar_temp = days.find('span', class_='month-calendar-temp').text.replace(' ', '').split('\n')[:2]
            except:
                calendar_temp = ["Нет данных", "Нет данных"]
                logging.error(f"Нет температуры. {days}")

            calendar_temp_morning = calendar_temp[0]
            calendar_temp_evening = calendar_temp[1]
                # logging.info(f"{calendar_day_chareds} : {calendar_month_chareds} - Утром = {calendar_temp_morning}. Вечером = {calendar_temp_evening}")
            result.append(
                {
                    "Год": 2025,
                    "Месяц": calendar_month_chareds,
                    "День": calendar_day_chareds,
                    "Погода утром": calendar_temp_morning,
                    "Погода вечером": calendar_temp_evening,
                }
            )
    return result


def save_csv(dann_temperatur):

    # Создание DataFrame
    df = pd.DataFrame(dann_temperatur)
    # Экспорт в CSV с помощью Pandas
    df.to_csv('output_with_pandas.csv', index=False, sep=";", mode='a', header=False, encoding='utf-8')
    logging.info("Данные сохранены в CSV")


if __name__ == '__main__':
    # pass
    save_csv(sampling_month())
