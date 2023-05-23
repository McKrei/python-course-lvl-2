Вот пример работы с модулем Unittest для тестирования простой функции деления:

```python
import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        result = divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

В этом примере у нас есть функция `divide`, которая делит одно число на другое. Мы определяем класс `DivideTestCase`, который наследуется от `unittest.TestCase` и содержит два метода тестирования: `test_divide` и `test_divide_by_zero`.

В методе `test_divide` мы вызываем функцию `divide` с аргументами 6 и 3 и проверяем, что результат равен 2, используя метод `self.assertEqual`.

В методе `test_divide_by_zero` мы ожидаем, что при попытке деления на ноль будет возбуждено исключение `ValueError`. Мы используем `self.assertRaises` для проверки этого.

Затем мы вызываем `unittest.main()`, чтобы запустить все тесты в классе `DivideTestCase`.

Выполнение этого файла в консоли или через IDE, поддерживающую Unittest, запустит тесты и выведет результаты, указывая, пройдены ли они успешно или нет.

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

Здесь `..` означает, что оба теста были успешно пройдены. Если бы один из тестов завершился неудачно, мы бы видели информацию об ошибке или несоответствии.
