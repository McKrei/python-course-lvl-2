## bs4
Библиотека BeautifulSoup4 (или просто bs4) - это Python-библиотека для парсинга HTML- и XML-документов. Она позволяет обрабатывать HTML-страницы и извлекать из них нужные данные, такие как заголовки, текст, ссылки и многое другое.

Чтобы использовать библиотеку bs4, сначала нужно установить ее. Это можно сделать с помощью пакетного менеджера pip:

```
pip install beautifulsoup4
```

Далее, импортируем библиотеку в наш код:

```python
from bs4 import BeautifulSoup
```

Теперь мы можем начать парсить HTML-страницы. Рассмотрим следующий пример HTML-кода:

```html
<html>
  <head>
    <title>Мой сайт</title>
  </head>
  <body>
    <h1>Добро пожаловать на мой сайт!</h1>
    <p>Это первый абзац.</p>
    <p>Это второй абзац.</p>
    <a href="http://example.com">Ссылка</a>
  </body>
</html>
```

Мы можем создать объект `BeautifulSoup`, который будет представлять этот HTML-код:

```python
html = """
<html>
  <head>
    <title>Мой сайт</title>
  </head>
  <body>
    <h1>Добро пожаловать на мой сайт!</h1>
    <p>Это первый абзац.</p>
    <p>Это второй абзац.</p>
    <a href="http://example.com">Ссылка</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
```

Первый аргумент функции `BeautifulSoup` - это HTML-код, который мы хотим распарсить. Второй аргумент - это парсер, который будет использоваться для парсинга. В данном случае мы используем стандартный парсер 'html.parser'.

Теперь мы можем использовать объект `soup`, чтобы извлечь нужные нам данные. Например, мы можем получить заголовок страницы:

```python
title = soup.title
print(title.text) # Мой сайт
```

Мы также можем получить все абзацы на странице:

```python
paragraphs = soup.find_all('p')
for p in paragraphs:
  print(p.text)
# Это первый абзац.
# Это второй абзац.
```

Мы можем получить ссылку на страницу:

```python
link = soup.find('a')
print(link['href']) # http://example.com
```

Также мы можем получить текст ссылки:

```python
print(link.text) # Ссылка
```

Еще примеры:

1. Получение всех ссылок на странице:

```python
links = soup.find_all('a')
for link in links:
  print(link['href'])
```

2. Получение всех заголовков на странице:

```python
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for heading in headings:
  print(heading.text)
```

3. Получение всех элементов с определенным классом:

```python
elements = soup.find_all(class_='my-class')
for element in elements:
  print(element.text)
```

4. Получение всех элементов с определенным именем тега и атрибутом:

```python
elements = soup.find_all('div', {'data-id': '123'})
for element in elements:
  print(element.text)
```

5. Получение всех элементов, которые содержат определенный текст:

```python
elements = soup.find_all(text='some text')
for element in elements:
  print(element)
```

6. Работа с деревом DOM HTML-документа:

```python
# Получение родительского элемента
parent = link.parent

# Получение всех дочерних элементов
children = parent.children

# Получение всех следующих элементов
next_elements = link.find_next_siblings()

# Получение всех предыдущих элементов
previous_elements = link.find_previous_siblings()
```


Библиотека BeautifulSoup4 предоставляет несколько способов поиска элементов на веб-странице. Рассмотрим некоторые из них:

1. Поиск по тегу:
Метод `find_all()` находит все элементы на странице, соответствующие заданному тегу:
```python
from bs4 import BeautifulSoup
import requests

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Найти все элементы <a>
a_tags = soup.find_all('a')
```

2. Поиск по классу:
Метод `find_all()` также может использоваться для поиска элементов по классу:
```python
# Найти все элементы с классом 'some-class'
elements = soup.find_all(class_='some-class')
```

3. Поиск по id:
Метод `find_all()` может использоваться для поиска элемента по id:
```python
# Найти элемент с id 'some-id'
element = soup.find_all(id='some-id')
```

4. Поиск по селектору CSS:
Метод `select()` находит элементы на странице, соответствующие заданному селектору CSS:
```python
# Найти все элементы с классом 'some-class' внутри элемента <div>
elements = soup.select('div .some-class')
```

5. Поиск по атрибутам:
Метод `find_all()` может использоваться для поиска элементов по атрибутам:
```python
# Найти все элементы, у которых есть атрибут 'data-attribute'
elements = soup.find_all(attrs={'data-attribute': True})
```

Множественный поиск элементов в BeautifulSoup4 можно осуществить, используя метод `find_all()` в комбинации с аргументами, переданными в виде словаря. Это позволяет искать элементы, которые соответствуют нескольким критериям одновременно.

Например, допустим, мы хотим найти все элементы `div`, которые имеют класс `class1` и атрибут `data-attribute` со значением `value1`. Мы можем использовать следующий код:

```python
elements = soup.find_all('div', {'class': 'class1', 'data-attribute': 'value1'})
```

Здесь мы передаем методу `find_all()` тег `'div'` в качестве первого аргумента и словарь, содержащий два ключа-значения, соответствующие классу и атрибуту элемента.

Также можно использовать операторы `|` (или) и `&` (и) для объединения нескольких критериев поиска:

```python
# Или
elements = soup.find_all('div', {'class': 'class1'} | {'data-attribute': 'value1'})

# И
elements = soup.find_all('div', {'class': 'class1'} & {'data-attribute': 'value1'})
```


