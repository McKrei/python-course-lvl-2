Задачи по Python и шаблон для тестирования:

1. Создание класса "Студент" с атрибутами "имя", "фамилия", "курс", "средний балл". Реализовать методы для добавления и удаления студента, изменения данных студента, вывода информации о всех студентах, а также поиска студента по фамилии.

Шаблон для тестирования:

```
# импортируем класс
class Student:
    ...

# создаем объекты студентов
student1 = Student("Иван", "Иванов", 3, 4.5)
student2 = Student("Петр", "Петров", 2, 3.7)

# добавляем студента
student3 = Student("Сергей", "Сергеев", 1, 4.0)
Student.add_student(student3)

# изменяем данные студента
student1.change_course(4)

# выводим информацию о всех студентах
Student.print_students()

# ищем студента по фамилии
Student.search_student("Иванов")
```

2. Создание класса "Калькулятор" с методами для выполнения математических операций (сложение, вычитание, умножение, деление). Реализовать также возможность сохранения результатов операций в памяти калькулятора и их отображения.

Шаблон для тестирования:

```
# импортируем класс
class Calculator:
    ...

# создаем объект калькулятора
calc = Calculator()

# выполняем операции
calc.add(5, 3)
calc.subtract(5, 3)
calc.multiply(5, 3)
calc.divide(5, 3)

# сохраняем результат в память калькулятора
calc.memorize_result()

# отображаем результаты операций
calc.show_results()

# отображаем результат, сохраненный в памяти калькулятора
calc.show_memory()
```

3. Создание класса "Телефонная книга" с атрибутами "имя", "номер телефона". Реализовать методы для добавления и удаления контакта, изменения данных контакта, вывода информации о всех контактах, а также поиска контакта по имени.

Шаблон для тестирования:

```
# импортируем класс
class Phonebook:
    ...


# создаем объекты контактов
contact1 = Phonebook("Иван Иванов", "+7 (111) 111-11-11")
contact2 = Phonebook("Петр Петров", "+7 (222) 222-22-22")

# добавляем контакт
contact3 = Phonebook("Сергей Сергеев", "+7 (333) 333-33-33")
Phonebook.add_contact(contact3)

# изменяем данные контакта
contact1.change_phone("+7 (444) 444-44-44")

# выводим информацию о всех контактах
Phonebook.print_contacts()

# ищем контакт по имени
Phonebook.search_contact("Петр Петров")
```