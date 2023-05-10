
class Student:
    students_list = []

    def __init__(self, first_name, last_name, course, average_score):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.average_score = average_score
        self.__class__.students_list.append(self)

    def change_course(self, new_course):
        self.course = new_course

    @classmethod
    def add_student(cls, student):
        cls.students_list.append(student)

    @classmethod
    def remove_student(cls, student):
        cls.students_list.remove(student)

    @classmethod
    def print_students(cls):
        for student in cls.students_list:
            print(f"{student.first_name} {student.last_name}, {student.course} курс, средний балл {student.average_score}")

    @classmethod
    def search_student(cls, last_name):
        is_stud = False
        for student in cls.students_list:
            if student.last_name == last_name:
                print(f"{student.first_name} {student.last_name}, {student.course} курс, средний балл {student.average_score}")
                is_stud = True

        if not is_stud:
            print(f"Студент с фамилией {last_name} не найден")


student1 = Student("Иван", "Иванов", 3, 4.5)
student2 = Student("Петр", "Петров", 2, 3.7)

student3 = Student("Сергей", "Сергеев", 1, 4.0)
Student.add_student(student3)

student1.change_course(4)

Student.print_students()

Student.search_student("Иванов")
