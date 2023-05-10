import requests
import json

def get(url, headers, params):
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        return resp
    return None


if __name__ == '__main__':
    url = 'https://search.wb.ru/exactmatch/ru/male/v4/search'
    params = {
        'appType': '1',
        'curr': 'rub',
        'dest': '-1281648',
        'query': 'кросы',
        'regions': '80,64,38,4,115,83,33,68,70,69,30,86,75,40,1,66,48,110,31,22,71,114',
        'resultset': 'catalog',
        'sort': 'popular',
        'spp': '22',
        'suppressSpellcheck': 'true',
        'page': '11',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    }
    resp = get(url, headers, params)
    dct = resp.json()
    print(type(dct))
    print(dct['metadata'])
    with open("wb.json", "w", encoding="utf-8") as f:
        json.dump(dct, f, ensure_ascii=False, indent=4)