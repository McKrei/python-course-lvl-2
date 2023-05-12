import multiprocessing
import requests
import time


def get_products(url):
    response = requests.get(url)
    return response.json()['data']['products']


if __name__ == '__main__':
    start = time.time()

    # Создаем пул процессов с помощью multiprocessing.Pool
    pool = multiprocessing.Pool()

    # Задаем список URL-адресов веб-страниц для загрузки
    urls = [
        f'https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query=%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D0%B2%D0%BA%D0%B8&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        for i in range(1, 61)
    ]

    # Используем метод map пула процессов для применения функции get_products к каждому URL-адресу
    # в списке urls с использованием нескольких процессов
    results = pool.map(get_products, urls)

    # Выводим результаты загрузки веб-страниц
    all_products = [product for result in results for product in result]
    print(time.time() - start)
    print(len(all_products))
