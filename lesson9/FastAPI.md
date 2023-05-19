FastAPI - это современный, быстрый (отсюда и название) и простой в использовании фреймворк для создания веб-приложений на языке Python. Он основывается на асинхронном сервере Starlette и использует типы данных Python 3.7+ для автоматической проверки запросов и ответов.

Вот подробный план, чтобы начать использовать FastAPI:

Шаг 1: Установка FastAPI
Первым делом необходимо установить FastAPI и его зависимости. Можно установить его с помощью пакетного менеджера pip, выполнив следующую команду:
```
pip install fastapi
```

Шаг 2: Создание простого приложения
Создайте новый файл Python с расширением `.py` и импортируйте необходимые модули:
```python
from fastapi import FastAPI
```
Затем создайте экземпляр приложения FastAPI:
```python
app = FastAPI()
```

Шаг 3: Определение маршрутов (роутинг)
FastAPI использует декораторы для определения маршрутов (роутинга) и обработчиков запросов. Например, чтобы создать маршрут `/`, используйте декоратор `app.get()` и определите соответствующую функцию-обработчик:
```python
@app.get("/")
def root():
    return {"message": "Hello, World!"}
```
В данном случае, при обращении к корневому URL будет возвращаться JSON-объект `{"message": "Hello, World!"}`.

Шаг 4: Запуск сервера
Для запуска сервера разместите следующий код в конце файла:
```python
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
Это запустит сервер на локальном хосте (localhost) с портом 8000.

Шаг 5: Запуск приложения
Запустите ваше приложение с помощью команды `python your_app_file.py` в командной строке. После этого ваше приложение будет доступно по адресу `http://localhost:8000/`.

Вы можете добавлять новые маршруты, создавая дополнительные функции-обработчики и используя различные методы HTTP, такие как `@app.post()`, `@app.put()`, `@app.delete()` и другие.

FastAPI также предоставляет подробную документацию и инструменты для автоматической генерации интерактивной документации API на основе типов данных и аннотаций функций. Вы можете ознакомиться с этими возможностями в официальной документации FastAPI.

Разберем пример сложного приложения на FastAPI с использованием схем. Допустим, мы хотим создать приложение для управления задачами (то-до списком).

Шаг 1: Установка зависимостей
Установим FastAPI и библиотеку для работы с базой данных SQLAlchemy:
```
pip install fastapi sqlalchemy
```

Шаг 2: Создание базы данных
Создадим простую базу данных SQLite, в которой будем хранить информацию о задачах. Создайте новый файл `database.py` и добавьте следующий код:
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Integer, default=False)
```
В этом коде мы создаем базу данных SQLite с помощью SQLAlchemy и определяем модель задачи (`Task`), которая содержит поля `id`, `title`, `description` и `completed`.

Шаг 3: Создание маршрутов и схем
Создайте новый файл `main.py` и добавьте следующий код:
```python
from fastapi import FastAPI
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Task
from .schemas import TaskCreateSchema, TaskUpdateSchema

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.middleware("http")
async def db_session_middleware(request, call_next):
    response = await call_next(request)
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreateSchema, db: Session = app.db):
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdateSchema, db: Session = app.db):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        for field, value in task.dict(exclude_unset=True).items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
        return db_task
    else:
        raise HTTPException(status_code=404, detail="Task not found")
```
В этом коде мы создаем два маршрута: `POST /tasks` для создания новой задачи и `PUT /tasks/{task_id}` для обновления существующей задачи по идентификатору. Мы используем схемы `TaskCreateSchema` и `TaskUpdateSchema` для проверки и валидации данных.

Шаг 4: Создание схем
Создайте новый файл `schemas.py` и добавьте следующий код:
```python
from pydantic import BaseModel


class TaskBaseSchema(Base

Model):
    title: str
    description: str


class TaskCreateSchema(TaskBaseSchema):
    pass


class TaskUpdateSchema(TaskBaseSchema):
    completed: bool
```
В этом коде мы определяем базовую схему `TaskBaseSchema`, которая содержит поля `title` и `description`. Затем мы создаем схемы `TaskCreateSchema` и `TaskUpdateSchema`, наследуясь от базовой схемы и добавляя поле `completed` для обновления задачи.

Шаг 5: Запуск приложения
В конце файла `main.py` добавьте следующий код для запуска сервера:
```python
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

Шаг 6: Тестирование приложения
Запустите приложение с помощью команды `python main.py`. Теперь вы можете использовать инструменты для тестирования API, например, Postman или curl.

Пример запросов:
- `POST /tasks`:
  ```json
  {
    "title": "Task 1",
    "description": "Description for Task 1"
  }
  ```
- `PUT /tasks/1`:
  ```json
  {
    "title": "Updated Task 1",
    "completed": true
  }
  ```

В этом примере мы создали сложное приложение на FastAPI для управления задачами с использованием схем для валидации данных. Вы можете расширить его, добавив дополнительные маршруты и функции, в зависимости от ваших потребностей.
