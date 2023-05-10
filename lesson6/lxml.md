lxml - это библиотека для обработки XML и HTML-документов на языке Python. Она предоставляет удобный и быстрый API для работы с данными в XML- и HTML-форматах, позволяя извлекать информацию из документов, преобразовывать их и создавать новые.

Lxml включает в себя два основных модуля: etree и html. etree - это модуль для работы с XML-документами, а html - для работы с HTML-документами. Оба модуля предоставляют одинаковый API для работы с деревом элементов, поэтому многие методы и функции могут быть использованы для работы с обоими типами документов.

Чтобы начать использовать lxml, необходимо сначала установить его через pip:

```
pip install lxml
```

Затем импортируем библиотеку в наш код:

```python
from lxml import etree, html
```

Для начала рассмотрим работу с XML-документами. Рассмотрим пример XML-документа:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J.K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
</bookstore>
```

Для создания дерева элементов используем функцию `etree.fromstring()`:

```python
xml = """
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J.K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
</bookstore>
"""

tree = etree.fromstring(xml)
```

Теперь мы можем использовать методы и функции из библиотеки lxml для работы с деревом элементов. Например, мы можем получить все элементы `book`:

```python
books = tree.xpath('//book')
for book in books:
  print(etree.tostring(book, encoding='unicode'))
```

Мы также можем получить атрибуты элементов:

```python
categories = tree.xpath('//book/@category')
for category in categories:
  print(category)
```

Кроме того, мы можем создавать новые элементы и добавлять их в дерево:

```python
new_book = etree.Element('book')
new_book.set('category', 'fiction')

