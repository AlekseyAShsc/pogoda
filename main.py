import logging
import time
# import datetime
# from datetime import date, timedelta
import random
from datetime import date, timedelta, datetime
from loader_url import reader_url_saved_text
from weathe_sampling import sampling_month, save_csv

logging.basicConfig(
    filename="pogoda.log",
    # format='%(asctime)s - %(filename)s - %(name)s -
    #           %(levelname)s - %(funcName)s - %(message)s',
    format='%(levelname)-8s [%(asctime)s] - %(filename)-25s:'
           '%(lineno)d - %(name)s - %(message)s',
    level=logging.ERROR
)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # https://pogoda1.ru/oktyabrsky-11/01-01/#year-2024 - 1 января
    # https://pogoda1.ru/oktyabrsky-11/02-01/#year-2024 - 2 января
    nacalo = datetime.now()  # время
    sleep_sum = 0  # сумарное время простоя
    kolvo = 0

    # Начальная дата
    start_date = date(2024, 1, 5)
    # Конечная дата
    end_date = date(2024, 1, 5)

    # Цикл по датам в формате 01-01
    for n in range(int((end_date - start_date).days)+1):
        data_range = (start_date + timedelta(n)).strftime('%d-%m')  # сада дата
        reader_url_saved_text(data_range)  # Сохраняем старницу
        # Читаем и выбирает нужные данные
        forecast_day_info, forecast_day_times = sampling_month()
        # Сохраняем в два файла выбранные данные
        save_csv(forecast_day_info, forecast_day_times)
        sleep_g = random.randint(6, 15)
        sleep_sum += sleep_g
        print(
            f'Пауза перед новым месяцем - {sleep_g} c.  / --------------{data_range}---------------/')
        logging.info(
            f'Пауза перед новым месяцем - {sleep_g} c. / --------------{data_range}---------------/')
        time.sleep(sleep_g)
    konec = datetime.now()
    print(f'{konec} - {nacalo} = {konec-nacalo}')
    logger.info(f"Общее время = {konec-nacalo}, из них пауз {sleep_sum}")
    print("Готово")
