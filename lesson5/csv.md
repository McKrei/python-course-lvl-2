## CSV

CSV (Comma-Separated Values) - это формат хранения данных в виде таблицы, где значения разделены запятыми. CSV-файлы могут использоваться для хранения и обмена данными между различными программами и системами.

В Python есть встроенный модуль csv для работы с данными в формате CSV. Рассмотрим некоторые основные операции с данными в формате CSV в Python.

#### Чтение данных из CSV-файла

Модуль csv предоставляет методы для чтения данных из CSV-файла. Например, если у нас есть файл example.csv, содержащий следующую таблицу:

```
Name, Age, City
John, 30, New York
Jane, 25, San Francisco
```

Мы можем считать его следующим образом:

```python
import csv

with open('example.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(', '.join(row))
```

Этот код прочитает CSV-файл и выведет его содержимое в консоль:

```
Name, Age, City
John, 30, New York
Jane, 25, San Francisco
```

Метод csv.reader() создает объект, который позволяет итерироваться по строкам CSV-файла. Он принимает несколько параметров, включая разделитель и символ, используемый для экранирования строковых значений.

#### Запись данных в CSV-файл

Модуль csv также предоставляет методы для записи данных в CSV-файл. Например, чтобы записать данные в CSV-файл, можно использовать следующий код:

```python
import csv

data = [
    ["Name", "Age", "City"],
    ["John", "30", "New York"],
    ["Jane", "25", "San Francisco"]
]

with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)
```

Этот код создаст CSV-файл с содержимым, аналогичным приведенному выше примеру.

Метод csv.writer() создает объект, который позволяет записывать данные в CSV-файл. Он принимает несколько параметров, включая разделитель и символ, используемый для экранирования строковых значений.

#### Доступ к данным в формате CSV

Данные в формате CSV представляют собой таблицу, где каждая строка содержит набор значений, разделенных запятыми. Для доступа к данным в формате CSV в Python можно использовать индексы и ключи.

Например, чтобы получить значение "Age" для первой строки в приведенном выше примере, можно использовать следующий код:

```python
import csv

with open('example.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        headers = next(reader)
        for row in reader:
            age = row[1]
            print(age)
```

Этот код прочитает CSV-файл и выведет значения второго столбца (возраст) для каждой строки, кроме первой (заголовков столбцов).

Если в таблице есть заголовки столбцов, то можно использовать их для доступа к данным в формате CSV. Например, чтобы получить значение "Age" для первой строки в приведенном выше примере, можно использовать следующий код:

```python
import csv

with open('example.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        age = row['Age']
        print(age)
```

Этот код прочитает CSV-файл и выведет значения столбца "Age" для каждой строки, используя заголовки столбцов для доступа к данным.

#### Изменение данных в формате CSV

Чтобы изменить данные в формате CSV в Python, нужно сначала считать данные из CSV-файла в объект Python, затем внести изменения и записать данные обратно в CSV-файл.

Например, чтобы изменить значение "Age" для первой строки в приведенном выше примере, можно использовать следующий код:

```python
import csv

with open('example.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    data = [row for row in reader]

data[1][1] = '31'

with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)
```

Этот код считает данные из CSV-файла в объект Python, изменит значение "Age" для первой строки на 31, а затем запишет данные обратно в CSV-файл.

#### Создание данных в формате CSV

Чтобы создать данные в формате CSV в Python, нужно создать объект Python, содержащий данные, и затем записать его в CSV-файл.

Например, для создания CSV-файла, содержащего информацию о двух людях, можно использовать следующий код:

```python
import csv

data = [
    ["Name", "Age", "City"],
    ["John", "30", "New York"],
    ["Jane", "25", "San Francisco"]
]

with open('example.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)
```

Этот код создаст CSV-файл с содержимым, аналогичным приведенному выше примеру.

