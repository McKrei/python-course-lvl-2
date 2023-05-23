Вот пример работы с фреймворком Pytest для тестирования той же функции деления:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide():
    result = divide(6, 3)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

В этом примере мы определяем две функции тестирования: `test_divide` и `test_divide_by_zero`. В каждой функции мы выполняем тестирование и используем утверждения (assertions) для проверки ожидаемых результатов.

В функции `test_divide` мы вызываем функцию `divide` с аргументами 6 и 3 и проверяем, что результат равен 2 с помощью `assert result == 2`.

В функции `test_divide_by_zero` мы ожидаем, что при попытке деления на ноль будет возбуждено исключение `ValueError`. Мы используем `pytest.raises(ValueError)` для проверки этого.

Затем мы можем запустить тесты, выполнив команду `pytest` в директории с файлом тестов или указав путь к файлу:

```
$ pytest test_divide.py
```

Результат выполнения будет выглядеть примерно так:

```
============================= test session starts ==============================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/tests
collected 2 items

test_divide.py ..                                                      [100%]

============================== 2 passed in 0.01s ===============================
```

Здесь `..` указывает, что оба теста были успешно пройдены. Если бы один из тестов завершился неудачно, мы бы видели информацию об ошибке или несоответствии.
