Задача 1: Написать программу, которая принимает на вход список чисел и возвращает список, содержащий только нечетные числа, умноженные на два. При этом, использовать функции `filter`, `map` и лямбда-функцию.


Тесты:
```python
def get_odd_doubled_numbers(numbers: list) -> list:
    pass

def test_get_odd_doubled_numbers():
    assert get_odd_doubled_numbers([1, 2, 3, 4, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([10, 20, 30]) == []
    assert get_odd_doubled_numbers([]) == []
    assert get_odd_doubled_numbers([1, 3, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([2, 4, 6]) == []
    print("All test_get_odd_doubled_numbers passed!")

test_get_odd_doubled_numbers()
```

Задача 2: Написать программу, которая считывает строку, проверяет, является ли она палиндромом, и выводит сообщение о результате проверки. При этом, использовать функции `reverse` и рекурсию.

Тесты:
```python
def check_palindrome(s: str) -> bool:
    pass

def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("level") == True
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("ab") == False
    print("All test_check_palindrome passed!")

test_check_palindrome()
```


Задача 3: Написать программу, которая принимает на вход список чисел и с помощью декоратора выводит время выполнения функции, которая сортирует его по возрастанию.

Тесты:
```python
from typing import List


def timer(func):
    pass


@timer
def sort_numbers(numbers: List[int]) -> List[int]:
    pass


def test_sort_numbers():
    assert sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert sort_numbers([]) == []
    assert sort_numbers([1]) == [1]
    assert sort_numbers([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert sort_numbers([1, 2, 3, 4]) == [1, 2, 3, 4]
    print("All test_sort_numbers pass")

test_sort_numbers()
```

Задача 4: Напишем рекурсивную функцию, которая вычисляет сумму цифр числа.

Тесты:
```python
def sum_of_digits(n: int) -> int:
    pass


def test_sum_of_digits():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(5) == 5
    assert sum_of_digits(10) == 1
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(999999999999999) == 135
    print("All test_sum_of_digits pass")

test_sort_numbers()
```
