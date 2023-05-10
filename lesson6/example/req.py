import requests
import bs4 as bs
import time


def get(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp
    return None




if __name__ == '__main__':
    # resp = get("https://www.gsmarena.com/xiaomi-phones-f-80-0-p2.php")
    # print(resp.status_code)
    # with open("p2.html", "w", encoding="utf-8") as f:
    #     f.write(resp.text)
    # with open("p2.html", "r", encoding="utf-8") as f:
    #     text = f.read()

    all_url = []
    for page in range(1, 10):
        url = f"https://www.gsmarena.com/xiaomi-phones-f-80-0-p{page}.php"
        resp = get(url)
        if resp:
            soup = bs.BeautifulSoup(resp.text, "lxml")
            makers = soup.find("div", class_="makers")
            a_all = makers.find_all("a")
            all_url += [f'https://www.gsmarena.com/{a["href"]}' for a in a_all]
            time.sleep(5)


    with open("all_url.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(all_url))