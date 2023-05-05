## JSON

JSON (JavaScript Object Notation) - это текстовый формат для обмена данными, основанный на синтаксисе объектов JavaScript. JSON используется для передачи структурированных данных между различными языками программирования, включая Python.

В Python есть встроенный модуль json для работы с данными в формате JSON. Рассмотрим некоторые основные операции с данными в формате JSON в Python.

#### Кодирование и декодирование JSON

Модуль json предоставляет методы для кодирования (преобразования объектов Python в JSON) и декодирования (преобразования JSON в объекты Python).

##### Кодирование

Метод json.dumps() преобразует объект Python в JSON-строку:

```python
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)

print(json_string)  # {"name": "John", "age": 30, "city": "New York"}
```

Метод json.dump() преобразует объект Python в JSON-строку и записывает ее в файл:

```python
with open('data.json', 'w') as f:
    json.dump(data, f)
```

##### Декодирование

Метод json.loads() преобразует JSON-строку в объект Python:

```python
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

data = json.loads(json_string)

print(data)  # {'name': 'John', 'age': 30, 'city': 'New York'}
```

Метод json.load() читает JSON-строку из файла и преобразует ее в объект Python:

```python
with open('data.json', 'r') as f:
    data = json.load(f)
```

#### Доступ к данным в формате JSON

Данные в формате JSON могут содержать объекты, массивы, строки, числа, логические значения и значения null. Для доступа к данным в формате JSON в Python можно использовать индексы и ключи.

Например, для доступа к значению "age" в приведенном выше примере можно использовать следующий код:

```python
age = data["age"]
print(age)  # 30
```

Если значение находится во вложенном объекте, то можно использовать несколько индексов:

```python
import json

json_string = '{"name": {"first": "John", "last": "Doe"}, "age": 30}'

data = json.loads(json_string)

first_name = data["name"]["first"]
print(first_name)  # John
```

#### Изменение данных в формате JSON

Чтобы изменить данные в формате JSON в Python, нужно сначала декодировать JSON-строку в объект Python, затем внести изменения и закодировать объект Python обратно в JSON-строку.

Например, чтобы изменить значение "age" в приведенном выше Примере, можно использовать следующий код:

```python
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'

data = json.loads(json_string)

data["age"] = 31

json_string = json.dumps(data)

print(json_string)  # {"name": "John", "age": 31, "city": "New York"}
```

#### Создание данных в формате JSON

Чтобы создать данные в формате JSON в Python, нужно создать объект Python и затем закодировать его в JSON-строку.

Например, для создания объекта, содержащего информацию о двух людях, можно использовать следующий код:

```python
import json

data = {
    "people": [
        {
            "name": "John",
            "age": 30,
            "city": "New York"
        },
        {
            "name": "Jane",
            "age": 25,
            "city": "San Francisco"
        }
    ]
}

json_string = json.dumps(data)

print(json_string)  # {"people": [{"name": "John", "age": 30, "city": "New York"}, {"name": "Jane", "age": 25, "city": "San Francisco"}]}
