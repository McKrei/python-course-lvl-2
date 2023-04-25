## Оператор присваивания

Оператор присваивания (`=`) в Python используется для присвоения значения переменной.

Например, чтобы присвоить значение 5 переменной `x`, вы можете использовать оператор присваивания следующим образом:

```python
x = 5
```

Здесь `x` - это переменная, которой присваивается значение 5.

Также вы можете использовать операторы присваивания в комбинации с другими операторами, чтобы выполнить операцию и присвоить результат переменной. Например:

```python
x = 10
x += 5   # Эквивалентно x = x + 5
print(x) # Выводит 15
```

Здесь оператор `+=` используется для сложения значения 5 с переменной `x` и присваивания результата обратно переменной `x`.

Python поддерживает также другие операторы присваивания, такие как `-=`, `*=`, `/=`, `//=`, `%=` и `**=`. Вот примеры:

```python
x = 10
x -= 3   # Эквивалентно x = x - 3
print(x) # Выводит 7

x *= 2   # Эквивалентно x = x * 2
print(x) # Выводит 14

x /= 3   # Эквивалентно x = x / 3
print(x) # Выводит 4.666666666666667

x //= 2  # Эквивалентно x = x // 2
print(x) # Выводит 2.0

x %= 2   # Эквивалентно x = x % 2
print(x) # Выводит 0.0

x **= 3  # Эквивалентно x = x ** 3
print(x) # Выводит 0.0
```

Оператор присваивания (`=`) также можно использовать для присваивания значений нескольким переменным одновременно, разделив значения запятой. Например:

```python
x, y, z = 1, 2, 3
```

Здесь переменной `x` присваивается значение 1, переменной `y` - значение 2, и переменной `z` - значение 3.

Также в Python можно использовать оператор присваивания для создания и присвоения значения переменной в одной строке. Например:

```python
x = y = z = 0
```

Здесь переменным `x`, `y` и `z` присваивается значение 0.

Еще одна интересная возможность оператора присваивания в Python - множественное присваивание. Например, вы можете присвоить значения нескольким переменным с помощью списка или кортежа. Например:

```python
values = [1, 2, 3]
x, y, z = values
```

Здесь переменным `x`, `y` и `z` присваиваются значения списка `values`.

Также в Python можно использовать оператор присваивания для обмена значениями двух переменных без использования временной переменной. Например:

```python
x = 10
y = 5

# Обмен значениями
x, y = y, x

print(x) # Выводит 5
print(y) # Выводит 10
```

Здесь значения переменных `x` и `y` меняются местами.

Оператор присваивания (`=`) - это основной оператор в Python, который используется для работы с переменными и объектами в языке.