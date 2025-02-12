import logging
import requests


logger = logging.getLogger(__name__)


# чтение данных с сайта и сохранение в файле index.html. Главная страница и страница модели
# https://pogoda1.ru/oktyabrsky-11/01-01/#year-2024 - 1 января
# https://pogoda1.ru/oktyabrsky-11/02-01/#year-2024 - 2 января
def reader_url_saved_text(data_url, prifiks="/#year-2024",  url_pogoda1="https://pogoda1.ru/oktyabrsky-11/"):
    # https://pogoda1.ru/oktyabrsky-11/january-2025/
    try:
        cookies = {
            '_gid': 'GA1.2.752516300.1738671137',
            '_ym_uid': '1738671137158730277',
            '_ym_d': '1738671137',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
            'home_city': 'eyJpdiI6IklQem5pNVFPbGFPNktmcG9jaHdMYWc9PSIsInZhbHVlIjoiaG5rVG1GY24xemNTTTF3XC96S2tNWlpkWnVNT3NOOEpKUWhmWkFoQkxZaFwvSDNMdnM2RWpHaTdxbk10MGdUd0RiIiwibWFjIjoiNjI4NDc4YTljY2NjZDEzYjJiYzhiNDcwZjFkOWM2YWQ4MTM1ODc0Y2IxY2FmMzBlZWY3OTZiYjA0YjkyOWZkZCJ9',
            '_ga': 'GA1.1.1966137014.1738671136',
            'XSRF-TOKEN': 'eyJpdiI6IlJBV2pabnFCVkhnXC9xS3VxeForMzdnPT0iLCJ2YWx1ZSI6InFuK2hEXC9QV0ljOHhmMXNBZ1NZM3A3SmpTQTNSNlJXR0E2dUZDTlV3elByR0NHOEhpRkdnQmw0QnFNcWdMN21jIiwibWFjIjoiMjc3MTc3MGUzZGYzZDdlZGE4MTZlMmVlNzcxMDU2MDBkZjExNmQ3NzI4ZDJjMWVjZTE5NjZlNGZkMzNjMTMxMyJ9',
            'laravel_session': 'eyJpdiI6IlVzdVNNZVwvdzNiZHh0ellLK1FxR2lRPT0iLCJ2YWx1ZSI6IkZOR2d2NmVMRjNPM3dzU1BkNGlwcXpPMjRFUFB3VCs4MEd2cXUrSGRzZ0lLMzl5UXFwMkVwNUlZNEIwc2NWdUE1eW5ESVJxaEd2UHdLbW15N0cyaklVdXBaWExqZElGSzFMSVc5OEFueUZ5SGhcL1dmUG9pTW1yNzdJUkNtaGpGSiIsIm1hYyI6IjYyOGJlOGRjMmYyY2YwYTQ5YTk4MWI5OGI1ODZlMzI4NDJmNDdmNDY5MGIzZmVlZDU1NTc1Yjg4NGE1YWZhMTgifQ%3D%3D',
            '_ga_XDQSF7786C': 'GS1.1.1738671135.1.1.1738672671.27.0.0',
        }
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': '_gid=GA1.2.752516300.1738671137; _ym_uid=1738671137158730277; _ym_d=1738671137; _ym_isad=2; _ym_visorc=w; home_city=eyJpdiI6IklQem5pNVFPbGFPNktmcG9jaHdMYWc9PSIsInZhbHVlIjoiaG5rVG1GY24xemNTTTF3XC96S2tNWlpkWnVNT3NOOEpKUWhmWkFoQkxZaFwvSDNMdnM2RWpHaTdxbk10MGdUd0RiIiwibWFjIjoiNjI4NDc4YTljY2NjZDEzYjJiYzhiNDcwZjFkOWM2YWQ4MTM1ODc0Y2IxY2FmMzBlZWY3OTZiYjA0YjkyOWZkZCJ9; _ga=GA1.1.1966137014.1738671136; XSRF-TOKEN=eyJpdiI6IlJBV2pabnFCVkhnXC9xS3VxeForMzdnPT0iLCJ2YWx1ZSI6InFuK2hEXC9QV0ljOHhmMXNBZ1NZM3A3SmpTQTNSNlJXR0E2dUZDTlV3elByR0NHOEhpRkdnQmw0QnFNcWdMN21jIiwibWFjIjoiMjc3MTc3MGUzZGYzZDdlZGE4MTZlMmVlNzcxMDU2MDBkZjExNmQ3NzI4ZDJjMWVjZTE5NjZlNGZkMzNjMTMxMyJ9; laravel_session=eyJpdiI6IlVzdVNNZVwvdzNiZHh0ellLK1FxR2lRPT0iLCJ2YWx1ZSI6IkZOR2d2NmVMRjNPM3dzU1BkNGlwcXpPMjRFUFB3VCs4MEd2cXUrSGRzZ0lLMzl5UXFwMkVwNUlZNEIwc2NWdUE1eW5ESVJxaEd2UHdLbW15N0cyaklVdXBaWExqZElGSzFMSVc5OEFueUZ5SGhcL1dmUG9pTW1yNzdJUkNtaGpGSiIsIm1hYyI6IjYyOGJlOGRjMmYyY2YwYTQ5YTk4MWI5OGI1ODZlMzI4NDJmNDdmNDY5MGIzZmVlZDU1NTc1Yjg4NGE1YWZhMTgifQ%3D%3D; _ga_XDQSF7786C=GS1.1.1738671135.1.1.1738672671.27.0.0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Opera";v="116", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0 (Edition Yx)',
        }
        url = f'{url_pogoda1}{data_url}{prifiks}'
        reg = requests.get(url, cookies=cookies, headers=headers)
        text_html = reg.text
        logging.info(f"Страница //{url}// выдалв ответ = {reg}.")
    except Exception as ex:
        logging.error(f"Ошибка, {ex}, при чтении страницы {url}")
    try:
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(text_html)
            # logging.info(f"Сnраница-{url} сохранена в файлe index.html")
        with open(f"url_all/index_{data_url}.html", "w", encoding="utf-8") as file:
            file.write(text_html)
            # logging.info(f"Сnраница-{url} сохранена в файл url_all\\index_{data_url}.html")
    except Exception as ex:
        logging.error(f"Ошибка, {ex}, при сохранении файла - url_all\\index_{data_url}.html")


if __name__ == '__main__':
    reader_url_saved_text("02-01")