## DB
CRUD - это аббревиатура, которая означает Create (Создание), Read (Чтение), Update (Обновление) и Delete (Удаление). Таблица CRUD представляет собой таблицу, которая позволяет выполнять все четыре операции CRUD для некоторой коллекции данных. Рассмотрим пример реализации таблицы CRUD в Python с использованием базы данных SQLite.


Библиотека sqlite3 предоставляет API для работы с базами данных SQLite в Python.

```python
import sqlite3

# Создание базы данных
connection = sqlite3.connect('example.db')

# Создание таблицы
connection.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Создание записи
def create_user(name, age):
    connection.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    connection.commit()

# Чтение записи
def read_user(id):
    cursor = connection.execute("SELECT * FROM users WHERE id=?", (id,))
    row = cursor.fetchone()
    return row

# Обновление записи
def update_user(id, name, age):
    connection.execute("UPDATE users SET name=?, age=? WHERE id=?", (name, age, id))
    connection.commit()

# Удаление записи
def delete_user(id):
    connection.execute("DELETE FROM users WHERE id=?", (id,))
    connection.commit()

# Пример использования
create_user("John", 30)
create_user("Jane", 25)

user = read_user(1)
print(user)

update_user(1, "Johnny", 31)

user = read_user(1)
print(user)

delete_user(1)

user = read_user(1)
print(user)

# Закрытие соединения
connection.close()
```

В этом примере мы создаем базу данных SQLite, создаем таблицу users, реализуем методы create_user(), read_user(), update_user() и delete_user() для выполнения операций CRUD, добавляем несколько записей, выполняем чтение, обновление и удаление записей и закрываем соединение с базой данных. Конечно, в более сложных приложениях, реализация CRUD-таблицы может быть более сложной, но этот пример демонстрирует основные концепции.
