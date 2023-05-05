## XLS и XLSX

XLS и XLSX - это форматы файлов, используемые для хранения электронных таблиц в Microsoft Excel.

Openpyxl - это библиотека для работы с файлами XLSX в Python, которая позволяет создавать, читать и записывать данные в файлы XLSX.

Вот примеры, как работать с библиотекой openpyxl:

#### Чтение данных из файла XLSX

Для чтения данных из файла XLSX с помощью библиотеки openpyxl необходимо использовать метод load_workbook(). Например, чтобы прочитать данные из файла example.xlsx и вывести их в консоль, можно использовать следующий код:

```python
import openpyxl

workbook = openpyxl.load_workbook('example.xlsx')
worksheet = workbook.active

for row in worksheet.iter_rows(values_only=True):
    print(row)
```

Метод iter_rows() возвращает итератор, который можно использовать для перебора строк в листе. Параметр values_only=True указывает на то, что метод должен возвращать только значения ячеек, а не объекты ячеек.

#### Запись данных в файл XLSX

Чтобы записать данные в файл XLSX с помощью библиотеки openpyxl, нужно создать объект Workbook(), добавить в него листы и заполнить их данными. Например, чтобы создать файл new.xlsx и заполнить его данными, можно использовать следующий код:

```python
import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.active

worksheet['A1'] = 'Name'
worksheet['B1'] = 'Age'
worksheet['C1'] = 'City'

worksheet.append(['John', 30, 'New York'])
worksheet.append(['Jane', 25, 'San Francisco'])

workbook.save('new.xlsx')
```

Этот код создаст новый файл new.xlsx и заполнит его данными.

#### Изменение данных в файле XLSX

Чтобы изменить данные в файле XLSX с помощью библиотеки openpyxl, нужно сначала прочитать данные из файла в объект Python, затем внести изменения и записать данные обратно в файл. Например, чтобы изменить значение ячейки A2 в файле example.xlsx, можно использовать следующий код:

```python
import openpyxl

workbook = openpyxl.load_workbook('example.xlsx')
worksheet = workbook.active

worksheet['A2'] = 'Jane'

workbook.save('example.xlsx')
```

Этот код откроет файл example.xlsx, изменит значение ячейки A2 на 'Jane' и сохранит изменения в файле.

Это лишь небольшой обзор работы с файлами XLS и XLSX и библиотекой openpyxl в Python. Openpyxl - это мощная библиотека для работы с файлами XLSX, которая позволяет создавать, читать и записывать данные в файлы XLSX в Python.
