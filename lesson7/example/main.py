import requests
import time


def get_products(url):
    # Получаем список продуктов из JSON-ответа на запрос
    products = requests.get(url).json()['data']['products']
    return products

def get_urls(query):
    # Генерируем список URL-адресов для запросов, включая параметры запроса и номера страницы
    urls = [
        f'https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query={query}&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
        for i in range(1, 61)
    ]
    return urls

all_products = []
start = time.time()

# Здесь должен быть код, который заполняет список all_products с помощью запросов
# к каждому URL-адресу из списка urls
# Но пока что список all_products остается пустым

def start_parsing():
    all_query = []
    # Здесь должен быть код, который заполняет список all_query
    # с нужными значениями запросов для парсинга

    for query in all_query:
        urls = get_urls(query)
        # Здесь должен быть код, который выполняет запросы к каждому URL-адресу
        # из списка urls и добавляет полученные продукты в список all_products

# Запускаем парсинг
start_parsing()

print(time.time() - start)
print(len(all_products))
