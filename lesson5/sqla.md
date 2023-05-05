## SQLAlchemy

SQLAlchemy - это библиотека на языке Python для работы с реляционными базами данных. Она предоставляет мощный и гибкий инструментарий для создания запросов к базе данных, а также для описания таблиц и связей между ними.

Вот пример простого использования SQLAlchemy для работы с базой данных SQLite:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# создаем подключение к базе данных SQLite
engine = create_engine('sqlite:///example.db')

# создаем объект-сессию, через который будем общаться с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# создаем базовый класс, от которого будут наследоваться все остальные классы-модели
Base = declarative_base()

# создаем класс-модель для таблицы users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# создаем таблицу в базе данных
Base.metadata.create_all(engine)

# добавляем запись в таблицу
user = User(name='John', age=30)
session.add(user)
session.commit()

# получаем записи из таблицы
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)
```

Здесь мы создаем подключение к базе данных SQLite, создаем объект-сессию для общения с базой данных, создаем класс-модель для таблицы пользователей, создаем таблицу в базе данных, добавляем запись в таблицу и получаем записи из таблицы.


## CRUD (Create, Read, Update, Delete)



Для примера, предположим, что у нас есть база данных, содержащая таблицу `users`, которая имеет следующую структуру:

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime)
```

Далее, давайте рассмотрим каждую из операций CRUD с использованием SQLAlchemy.

### Create (создание)

Чтобы создать новую запись в таблице `users`, необходимо создать объект модели `User` с заполненными атрибутами и добавить его в сессию для сохранения в базе данных. Пример:

```python
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='John Doe', email='john.doe@example.com', created_at=datetime.now())
session.add(new_user)
session.commit()
```

### Read (чтение)

Для чтения данных из таблицы `users` мы можем использовать различные методы объекта `session`. Например, метод `query` возвращает объект запроса, который можно использовать для выполнения различных операций чтения, например, для получения всех записей в таблице:

```python
users = session.query(User).all()
```

Этот код вернет список всех объектов `User`, содержащихся в таблице `users`.

Также мы можем использовать метод `filter` для выполнения фильтрации записей. Например, чтобы получить только пользователей, созданных после определенной даты, мы можем написать следующий код:

```python
from datetime import datetime

users = session.query(User).filter(User.created_at > datetime(2021, 1, 1)).all()
```

### Update (обновление)

Чтобы обновить запись в таблице `users`, мы можем сначала получить объект модели `User` с помощью метода `query`, изменить его атрибуты и затем вызвать метод `commit` объекта `session` для сохранения изменений в базе данных. Пример:

```python
user = session.query(User).filter_by(name='John Doe').first()
user.email = 'new.email@example.com'
session.commit()
```

### Delete (удаление)

Чтобы удалить запись из таблицы `users`, мы можем сначала получить объект модели `User`, который нужно удалить, используя метод `query`, а затем вызвать метод `delete` объекта `session` для удаления записи из базы данных. Пример:

```python
user = session.query(User).filter_by(name='John Doe').first()
session.delete(user)
session.commit()
```

Связь "один ко многим" (one-to-many) - это тип отношения между двумя таблицами в реляционных базах данных, при котором каждая запись в одной таблице может иметь несколько связанных записей в другой таблице, но каждая запись во второй таблице связана только с одной записью в первой таблице.

Примером связи "один ко многим" может быть таблица `Author`, содержащая информацию об авторах, и таблица `Book`, содержащая информацию о книгах, написанных этими авторами. Один автор может написать множество книг, но каждая книга связана только с одним автором.

В SQLAlchemy связь "один ко многим" может быть установлена с помощью отношения `relationship`. Для примера рассмотрим модель `Author` и `Book`:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
```

В этом примере мы создаем две таблицы: `authors` и `books`. У таблицы `books` есть столбец `author_id`, который является внешним ключом, связывающим каждую книгу с определенным автором. Столбец `books` в классе `Author` устанавливает отношение "один ко многим" между таблицами `authors` и `books`.

Теперь мы можем создавать новых авторов и книги, связанные с ними, используя объекты моделей и методы `add` и `commit` объекта `session`. Например:

```python
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# создаем нового автора
author = Author(name='Leo Tolstoy')
session.add(author)
session.commit()

# создаем новую книгу, связанную с автором
book = Book(title='War and Peace', author_id=author.id)
session.add(book)
session.commit()

# получаем всех авторов и связанные с ними книги
authors = session.query(Author).all()
for author in authors:
    print(author.name)
    for book in author.books:
        print(' - ', book.title)
```


Связь "многие ко многим" (many-to-many) - это тип отношения между двумя таблицами в реляционных базах данных, при котором каждая запись в одной таблице может быть связана с несколькими записями в другой таблице, и наоборот, каждая запись во второй таблице может быть связана с несколькими записями в первой таблице.

Примером связи "многие ко многим" может быть таблица `Student`, содержащая информацию о студентах, и таблица `Course`, содержащая информацию о курсах, которые эти студенты могут посещать. Каждый студент может записаться на несколько курсов, и каждый курс может быть посещен несколькими студентами.

В SQLAlchemy связь "многие ко многим" реализуется через использование дополнительной таблицы, которая связывает две таблицы в соответствии с их связью. Для этого используется класс `Table` из модуля `sqlalchemy.schema`, который представляет собой таблицу без класса модели. В классах модели для каждой таблицы указывается отношение `relationship`, которое ссылается на дополнительную таблицу.

Для примера рассмотрим модель `Student` и `Course` с промежуточной таблицей `student_courses`:

```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=student_courses)

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary=student_courses)
```

В этом примере мы создаем две таблицы: `students` и `courses`, а также промежуточную таблицу `student_courses`. Столбцы `student_id` и `course_id` в таблице `student_courses` являются внешними ключами, связывающими таблицы `students` и `courses`. Классы `Student` и `Course` устанавливают отношение "многие ко многим" между таблицами `students` и `courses`, используя свойство `secondary` для указания на промежуточную таблицу.

Теперь мы можем создавать новых студентов и курсы, связанные с ними, используя объекты моделей и методы `add` и `commit` объекта `session`. Например:

Мы можем создать нового студента и курсы, связанные с ним, используя следующий код:

```python
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# создаем нового студента
student = Student(name='John Doe')
session.add(student)
session.commit()

# создаем новые курсы и связываем их со студентом
course1 = Course(name='Math')
course2 = Course(name='Science')
student.courses.extend([course1, course2])
session.commit()

# получаем всех студентов и связанные с ними курсы
students = session.query(Student).all()
for student in students:
    print(student.name)
    for course in student.courses:
        print(' - ', course.name)
```

В этом примере мы создаем нового студента `John Doe`, затем создаем новые курсы `Math` и `Science` и связываем их со студентом, используя список `courses` объекта модели `Student`. Затем мы сохраняем изменения в базе данных и получаем всех студентов и связанные с ними курсы.

Также мы можем получить список всех студентов, которые записались на определенный курс, используя метод `filter` объекта `session`. Например, чтобы получить всех студентов, записавшихся на курс `Math`, мы можем написать следующий код:

```python
students = session.query(Student).join(Student.courses).filter(Course.name == 'Math').all()
for student in students:
    print(student.name)
```

В этом примере мы объединяем таблицы `students` и `courses` с помощью метода `join` объекта `query`, затем фильтруем записи по имени курса и получаем всех студентов, записавшихся на этот курс.
