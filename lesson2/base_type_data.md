## Базовые типы данных и их методы

Python - это высокоуровневый язык программирования, который поддерживает множество базовых типов данных, таких как числа, строки, списки, кортежи и словари. В этом блоке урока мы рассмотрим каждый тип данных, а также основные методы, которые могут быть применены к каждому типу данных.

### Числовые типы данных

Python поддерживает три типа числовых данных: целые числа (int), числа с плавающей точкой (float) и комплексные числа (complex).

#### Целые числа (int)

Целые числа представляются в Python с помощью типа данных int. Вот несколько примеров:

```python
x = 10
y = -5
```

##### Основные методы

- `abs(x)` - возвращает абсолютное значение x.
- `pow(x, y)` - возвращает x в степени y.
- `divmod(x, y)` - возвращает частное и остаток от деления x на y.
- `int(x)` - преобразует x в целое число.

#### Числа с плавающей точкой (float)

Числа с плавающей точкой представляются в Python с помощью типа данных float. Вот несколько примеров:

```python
x = 3.14
y = -0.5
```

##### Основные методы

- `abs(x)` - возвращает абсолютное значение x.
- `pow(x, y)` - возвращает x в степени y.
- `round(x)` - округляет x до ближайшего целого числа.

#### Комплексные числа (complex)

Комплексные числа представляются в Python с помощью типа данных complex. Вот несколько примеров:

```python
x = 3 + 5j
y = 2 - 3j
```

##### Основные методы

- `real(x)` - возвращает действительную часть комплексного числа x.
- `imag(x)` - возвращает мнимую часть комплексного числа x.
- `conjugate(x)` - возвращает комплексное сопряжение числа x.

### Строковые типы данных

Строки в Python представляются в виде последовательности символов в кавычках. Python поддерживает как одинарные ('), так и двойные (") кавычки для обозначения строк. Вот несколько примеров:

```python
x = 'Hello, world!'
y = "Python is awesome"
```

##### Основные методы

- `capitalize()` - возвращает строку с заглавной буквой в начале.
- `lower()` - преобразует все символы строки в нижний регистр.
- `upper()` - преобразует все символы  строки в верхний регистр.
- `strip()` - удаляет пробелы в начале и конце строки.
- `replace(old, new)` - заменяет все вхождения подстроки old на new.
- `split()` - разбивает строку на список подстрок по заданному разделителю.

### Списки

Списки в Python представляются в виде упорядоченной коллекции элементов, которые могут быть любого типа данных. Вот несколько примеров:

```python
x = [1, 2, 3, 4, 5]
y = ['apple', 'banana', 'cherry']
```

##### Основные методы

- `append(x)` - добавляет элемент x в конец списка.
- `insert(i, x)` - вставляет элемент x на позицию i в списке.
- `pop(i)` - удаляет элемент на позиции i и возвращает его значение.
- `sort()` - сортирует список по возрастанию.

### Кортежи

Кортежи в Python представляются в виде упорядоченной коллекции элементов, которые могут быть любого типа данных, но не могут быть изменены после создания. Вот несколько примеров:

```python
x = (1, 2, 3, 4, 5)
y = ('apple', 'banana', 'cherry')
```

##### Основные методы

Кортежи не имеют методов, но вы можете использовать некоторые из методов, которые доступны для списков, например, `len()` для получения длины кортежа.

### Словари

Словари в Python представляются в виде неупорядоченной коллекции пар ключ-значение. Вот несколько примеров:

```python
x = {'name': 'John', 'age': 25, 'city': 'New York'}
y = {1: 'apple', 2: 'banana', 3: 'cherry'}
```

##### Основные методы

- `get(key)` - возвращает значение для заданного ключа. Если ключ не найден, возвращает значение по умолчанию (None).
- `keys()` - возвращает список всех ключей в словаре.
- `values()` - возвращает список всех значений в словаре.
- `items()` - возвращает список кортежей (ключ, значение) для всех элементов в словаре.

Это только небольшая часть методов и функций, доступных для каждого типа данных в Python. Более подробную информацию можно найти в официальной документации Python.


https://docs.python.org/3/library/datatypes.html