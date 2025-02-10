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
    month_period = bs.find_all('div', class_='row-forecast-day-wrap row-forecast-day-collapsible opened')
    # logging.info(f"mont/h_period = {month_period}")
    forecast_day_info, forecast_day_times = [], []
    for days in month_period:
        try:
            date_day = days.find('div', class_='forecast-day-name').text.split()
            # logging.info(date_day)
            calendar_year_chareds = date_day[-1]
            calendar_month_chareds = date_day[-2]
            calendar_day_chareds = date_day[-3]
            logging.info(f"{calendar_year_chareds}/{calendar_month_chareds}/{calendar_day_chareds}")
            # calendar_month = (days['href']).split('/')[2]
            # calendar_month_chareds = int(calendar_month.split('-')[1])
        except:
            calendar_year_chareds = 0
            calendar_month_chareds = "месяц"
            calendar_day_chareds = 0
            logging.error(f"Нет даты.")
        try:
            info_day = [x.get_text() for x in (days.find_all('span', class_='value'))]
            info_visibl = info_day[0]
            info_moon = info_day[1]
            info_sun = info_day[2]
            logging.info(f"Видимость-{info_visibl},луна -{info_moon}, солнце - {info_sun}")
        except:
            info_visibl = "нет данных"
            info_moon = "нет данных"
            info_sun = "нет данных"
            logging.error(f"Нет данных. Видимость-{info_visibl},луна -{info_moon}, солнце - {info_sun}")

        # try:
        #     info_visibl = int(calendar_month.split('-')[0])
        # except:
        #     info_visibl = "нет данных"
        #     logging.error(f"Нет дня. {days}")



    #     try:
    #         calendar_day_chareds = int(calendar_month.split('-')[0])
    #     except:
    #         calendar_day_chareds = "нет данных"
    #         logging.error(f"Нет дня. {days}")
    #     try:
    #         calendar_temp = days.find('span', class_='month-calendar-temp').text.replace(' ', '').split('\n')[:2]
    #     except:
    #         calendar_temp = ["Нет данных", "Нет данных"]
    #         logging.error(f"Нет температуры. {days}")

    #     calendar_temp_morning = calendar_temp[0]
    #     calendar_temp_evening = calendar_temp[1]
    #         # logging.info(f"{calendar_day_chareds} : {calendar_month_chareds} - Утром = {calendar_temp_morning}. Вечером = {calendar_temp_evening}")
            """
            На всякий пожарный
            >>> html = '<html><div><p>hello world 1</p></div><div><p>hello world 2</p></div> </html>'
            >>> re.findall(r'<p>([^<]+)</p>', html)
            ['hello world 1', 'hello world 2']
            """

        forecast_day_info.append(
            {
            "Год": calendar_year_chareds,
            "Месяц": calendar_month_chareds,
            "День": calendar_day_chareds,
            "Видимость": info_visibl,
            "Луна": info_moon,
            "Солнце": info_sun,
            }
        )
    #         forecast_day_times.append(
    #             {
    #             "Год": calendar_year_chareds,
    #             "Месяц": calendar_month_chareds,
    #             "День": calendar_day_chareds,
    #             "Время": cell-forecast-time,
    #             "Погода": cell-forecast-main,
    #             "Температура": cell-forecast-temp,
    #             "Направление верта": cell-forecast-wind-direction,
    #             "Сила ветра": cell-forecast-wind-strength,
    #             "Давление": cell-forecast-press,
    #             "Влажность": cell-forecast-hum,
    #             "Осадки": cell-forecast-prec,
    #             }
    #         )
    return forecast_day_info, forecast_day_times

"""
forecast_day_info.append(
{
"Год": calendar_year_chareds,
"Месяц": calendar_month_chareds,
"День": calendar_day_chareds,
"Видимость": info_visibl,
"Луна": info_moon,
"Солнце": info_sun,
}
forecast-day-times.append(
{
"Год": calendar_year_charedsct,
"Месяц": calendar_month_chareds,
"День": calendar_day_chareds,
"Время": cell-forecast-time,
"Погода": cell-forecast-main,
"Температура": cell-forecast-temp,
"Направление верта": cell-forecast-wind-direction,
"Сила ветра": cell-forecast-wind-strength,
"Давление": cell-forecast-press,
"Влажность": cell-forecast-hum,
"Осадки": cell-forecast-prec,
}
)


"""




def save_csv(dann_temperatur):

    # Создание DataFrame
    df = pd.DataFrame(dann_temperatur)
    # Экспорт в CSV с помощью Pandas
    df.to_csv('output_with_pandas.csv', index=False, sep=";", mode='a', header=False, encoding='utf-8')
    logging.info("Данные сохранены в CSV")


if __name__ == '__main__':
    # pass
    # save_csv(sampling_month())
    print(sampling_month())