import logging
from bs4 import BeautifulSoup
import pandas as pd


# logging.basicConfig(
#     filename="pogoda.log",
#     # format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s',
#     format= '%(levelname)-8s [%(asctime)s] - %(filename)-25s:'\
#         '%(lineno)d - %(name)s - %(message)s',
#     level=logging.DEBUG,
#     filemode="w"
# )

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
        for time_of_day in days.find_all('div', class_='row-forecast-time-of-day'):
            # logging.info(f"logging.info = {time_of_day}")
            try:
                cell_forecast_time = time_of_day.find('div', class_='cell-forecast-time').text
                logging.info(f"Время = {cell_forecast_time}")
            except:
                cell_forecast_time = "нет данных"
                logging.error(f"Нет данных по временни. {calendar_day_chareds}:{calendar_month_chareds}:{calendar_year_chareds} на {cell_forecast_time}")
            try:
                cell_forecast_main = time_of_day.find('div', class_='cell-forecast-main').text.replace('\n', '')
                logging.info(f"Облачность = {cell_forecast_main}")
            except:
                cell_forecast_main = "нет данных"
                logging.error(f"Нет данных по облочности. {calendar_day_chareds}:{calendar_month_chareds}:{calendar_year_chareds} на {cell_forecast_time}")
            try:
                cell_forecast_temp = time_of_day.find('div', class_='cell-forecast-temp').text
                logging.info(f"Температура = {cell_forecast_temp}")
            except:
                cell_forecast_temp = "нет данных"
                logging.error(f"Нет данных по температуры. {calendar_day_chareds}:{calendar_month_chareds}:{calendar_year_chareds} на {cell_forecast_time}")
            cell_forecast_wind = time_of_day.find('div', class_='cell-forecast-wind')
            try:
                cell_forecast_wind_direction = cell_forecast_wind.img['title']
                logging.info(f"Направление ветра = {cell_forecast_wind_direction}")
            except:
                cell_forecast_wind_direction = "нет данных"
                logging.error(f"Нет данных по направлению ветра. {calendar_day_chareds}:{calendar_month_chareds}:{calendar_year_chareds} на {cell_forecast_time}")
            try:
                cell_forecast_wind_strength = cell_forecast_wind.find('span', class_='wind-amount').text
                logging.info(f"Сила ветра = {cell_forecast_wind_strength}")
            except:
                cell_forecast_wind_strength = "нет данных"
                logging.error(f"Нет данных по силе ветра. {calendar_day_chareds}:{calendar_month_chareds}:{calendar_year_chareds} на {cell_forecast_time}")

            try:
                cell_forecast_press = time_of_day.find('div', class_='cell-forecast-press').text
                logging.info(f"Давление = {cell_forecast_press}")
            except:
                cell_forecast_press = "нет данных"
                logging.error(f"Нет данных по давлению. {calendar_day_chareds}:{calendar_month_chareds}:{calendar_year_chareds} на {cell_forecast_time}")
            try:
                cell_forecast_hum = time_of_day.find('div', class_='cell-forecast-hum').text
                logging.info(f"Влажность = {cell_forecast_hum}")
            except:
                cell_forecast_hum = "нет данных"
                logging.error(f"Нет данных по влажности. {calendar_day_chareds}:{calendar_month_chareds}:{calendar_year_chareds} на {cell_forecast_time}")
            try:
                cell_forecast_prec = time_of_day.find('div', class_='cell-forecast-prec').text
                logging.info(f"Осадки = {cell_forecast_hum}")
            except:
                cell_forecast_prec = "нет данных"
                logging.error(f"Нет данных по осадкам. {calendar_day_chareds}:{calendar_month_chareds}:{calendar_year_chareds} на {cell_forecast_time}")

            forecast_day_times.append(
                {
                "Год": calendar_year_chareds,
                "Месяц": calendar_month_chareds,
                "День": calendar_day_chareds,
                "Время": cell_forecast_time,
                "Погода": cell_forecast_main,
                "Температура": cell_forecast_temp,
                "Направление верта": cell_forecast_wind_direction,
                "Сила ветра": cell_forecast_wind_strength,
                "Давление": cell_forecast_press,
                "Влажность": cell_forecast_hum,
                "Осадки": cell_forecast_prec,
                }
            )

            """
            На всякий пожарный
            print(soup.a['data-peer-id'])
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

    return forecast_day_info, forecast_day_times


def save_csv(forecast_day_info, forecast_day_times):
    try:
        # Создание DataFrame
        dfi = pd.DataFrame(forecast_day_info)
        # Экспорт в CSV с помощью Pandas
        dfi.to_csv('forecast_day_info.csv', index=False, sep=";", mode='a', header=False, encoding='utf-8')
        logging.info("Данные forecast_day_info сохранены в CSV")
    except:
        logging.error(f"Ошибка сохранения файла forecast_day_info.csv.")

    try:
        # Создание DataFrame
        dfd = pd.DataFrame(forecast_day_times)
        # Экспорт в CSV с помощью Pandas
        dfd.to_csv('forecast_day_times.csv', index=False, sep=";", mode='a', header=False, encoding='utf-8')
        logging.info("Данные forecast_day_times сохранены в CSV")
    except:
        logging.error(f"Ошибка сохранения файла forecast_day_times.csv.")



if __name__ == '__main__':
    # pass
    # save_csv(sampling_month())
    derrsd, sdfdfdsf = sampling_month()
    save_csv(derrsd, sdfdfdsf)
    print("Готово")