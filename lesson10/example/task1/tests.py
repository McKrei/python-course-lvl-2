# Импортируем необходимые модули и функции
import pytest
from my_module import add_numbers

# Определяем тестовый случай
def test_add_numbers():
    # Задаем входные данные и ожидаемый результат
    a = 5
    b = 3
    expected_result = 8

    # Вызываем функцию, которую тестируем
    result = add_numbers(a, b)

    # Проверяем результат с использованием утверждения
    assert result == expected_result
