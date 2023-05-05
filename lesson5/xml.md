## XML

XML - это язык разметки, который используется для представления и передачи структурированных данных в удобном для чтения человеком формате. В Python есть несколько способов работы с данными в формате XML. Рассмотрим некоторые из них.

Сначала необходимо импортировать модуль xml.etree.ElementTree:

```python
import xml.etree.ElementTree as ET
```

#### Чтение XML-файла

Для чтения XML-файла в Python можно использовать метод parse() модуля ElementTree. Например, если у нас есть файл example.xml, содержащий следующий XML-код:

```xml
<?xml version="1.0"?>
<catalog>
  <book id="bk101">
    <author>Gambardella, Matthew</author>
    <title>XML Developer's Guide</title>
    <genre>Computer</genre>
    <price>44.95</price>
    <publish_date>2000-10-01</publish_date>
    <description>An in-depth look at creating applications
      with XML.</description>
  </book>
  <book id="bk102">
    <author>Ralls, Kim</author>
    <title>Midnight Rain</title>
    <genre>Fantasy</genre>
    <price>5.95</price>
    <publish_date>2000-12-16</publish_date>
    <description>A former architect battles corporate zombies,
      an evil sorceress, and her own childhood to become queen
      of the world.</description>
  </book>
</catalog>
```

Мы можем считать его следующим образом:

```python
tree = ET.parse('example.xml')
root = tree.getroot()
```

Теперь переменная `root` содержит корневой элемент XML-документа.

#### Доступ к элементам XML

Чтобы получить доступ к элементам XML, можно использовать методы find() и findall(). Метод find() возвращает первый элемент с заданным тегом, а метод findall() возвращает список всех элементов с заданным тегом.

Например, чтобы получить все элементы "book" из XML-файла, можно использовать следующий код:

```python
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    price = book.find('price').text
    print(title, author, price)
```

#### Создание XML-файла

Для создания XML-файла в Python можно использовать модуль ElementTree. Вот пример создания простого XML-документа:

```python
import xml.etree.ElementTree as ET

root = ET.Element("catalog")

book1 = ET.SubElement(root, "book")
book1.set("id", "bk101")

author1 = ET.SubElement(book1, "author")
author1.text = "Gambardella, Matthew"

title1 = ET.SubElement(book1, "title")
title1.text = "XML Developer's Guide"

book2 = ET.SubElement(root, "book")
book2.set("id", "bk102")

author2 = ET.SubElement(book2, "author")
author2.text = "Ralls, Kim"

title2 = ET.SubElement(book2, "title")
title2.text = "Midnight RainМожно сохранить созданный XML-документ в файл следующим образом:

```python
tree = ET.ElementTree(root)
tree.write("catalog.xml")
```

Это создаст файл "catalog.xml" со следующим содержимым:

```xml
<catalog>
    <book id="bk101">
        <author>Gambardella, Matthew</author>
        <title>XML Developer's Guide</title>
    </book>
    <book id="bk102">
        <author>Ralls, Kim</author>
        <title>Midnight Rain</title>
    </book>
</catalog>
```

#### Изменение XML-документа

Чтобы изменить XML-документ, можно использовать методы set() и text. Например, чтобы изменить значение элемента "title" для первой книги в приведенном выше XML-документе, можно использовать следующий код:

```python
root.findall("./book[@id='bk101']/title")[0].text = "New title"
```

Это изменит значение элемента "title" для первой книги на "New title".

#### Удаление элементов XML

Чтобы удалить элементы из XML-документа, можно использовать метод remove(). Например, чтобы удалить элемент "book" с идентификатором "bk102" из XML-документа, можно использовать следующий код:

```python
book_to_delete = root.find("./book[@id='bk102']")
root.remove(book_to_delete)
```

Это удалит элемент "book" с идентификатором "bk102" из XML-документа.

