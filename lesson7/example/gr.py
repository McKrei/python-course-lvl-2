import grequests
import time

start = time.time()

urls = [
    f'https://search.wb.ru/exactmatch/ru/male/v4/search?appType=1&curr=rub&dest=-1281648&page={i}&query=%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D0%B2%D0%BA%D0%B8&regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114&resultset=catalog&sort=popular&spp=22&suppressSpellcheck=false'
    for i in range(1, 61)
]

# Создаем объекты запросов для каждого URL-адреса
requests = (grequests.get(u) for u in urls)

# Выполняем асинхронные запросы с использованием grequests.map
responses = grequests.map(requests)

# Извлекаем данные из каждого ответа и сохраняем их в список продуктов
products = [product for response in responses for product in response.json()['data']['products']]

print("Время выполнения:", time.time() - start)
print("Количество продуктов:", len(products))
