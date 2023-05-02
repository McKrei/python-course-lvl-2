Шаблоны проектирования - это повторно используемые решения для общих задач при проектировании программного обеспечения. Шаблоны проектирования можно разделить на три категории: порождающие (creational), структурные (structural) и поведенческие (behavioral).


## Singleton
Одним из практических применений метода `__new__()` может быть создание синглтона - класса, для которого должен существовать только один объект. В таком случае при каждом вызове конструктора класса мы будем возвращать тот же самый объект, а не создавать новый.

Вот пример реализации синглтона с помощью метода `__new__()`:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # выводит True
```

Здесь мы создаем класс `Singleton`, который имеет статическую переменную `_instance`, которая хранит единственный экземпляр класса. При создании нового объекта класса мы проверяем, существует ли уже объект `_instance`. Если да, то мы возвращаем этот объект, а если нет, то создаем новый объект, сохраняем его в `_instance` и возвращаем его.

Таким образом, при каждом создании нового объекта класса `Singleton`, мы будем получать тот же самый объект, созданный при первом вызове конструктора. В результате, `singleton1` и `singleton2` - это один и тот же объект, что мы можем проверить, используя оператор `is`.

Такой подход к созданию синглтона может быть полезен, например, для создания объектов, которые являются настройками приложения, базами данных или кэшами.

Рассмотрим пример использования синглтона для хранения настроек приложения:

```python
class AppConfig:
    _instance = None
    _settings = {
        'theme': 'dark',
        'language': 'en'
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def theme(self):
        return self._settings['theme']

    @theme.setter
    def theme(self, value):
        self._settings['theme'] = value

    @property
    def language(self):
        return self._settings['language']

    @language.setter
    def language(self, value):
        self._settings['language'] = value
```

Здесь мы создаем класс `AppConfig`, который является синглтоном. У этого класса есть статический метод `_instance`, который хранит единственный экземпляр класса. Кроме того, у класса есть статическое свойство `_settings`, которое хранит настройки приложения.

Мы определяем метод `__new__()` для класса `AppConfig`, чтобы гарантировать, что будет создан только один экземпляр класса. Затем мы определяем методы доступа к настройкам приложения с помощью декораторов `@property` и `@<property>.setter`. Эти методы позволяют нам получать и устанавливать значения настроек приложения.

Теперь мы можем использовать объект класса `AppConfig` во всем приложении, чтобы хранить и получать настройки приложения:

```python
config = AppConfig()
config.theme = 'light'
config.language = 'ru'

print(config.theme)     # выводит "light"
print(config.language)  # выводит "ru"

config2 = AppConfig()
print(config2.theme)    # выводит "light"
print(config2.language) # выводит "ru"
```

Здесь мы создаем объект `config` класса `AppConfig` и устанавливаем настройки приложения. Затем мы создаем новый объект `config2` того же класса и получаем те же самые настройки, что мы установили в `config`. Это происходит потому, что класс `AppConfig` является синглтоном, и при каждом создании нового объекта мы получаем тот же самый экземпляр класса.


## Порождающие шаблоны проектирования

Порождающие шаблоны проектирования (creational patterns) используются для создания объектов и группировки объектов в более крупные структуры. Некоторые из наиболее распространенных порождающих шаблонов проектирования в Python:

1. Фабричный метод (Factory Method) - это порождающий шаблон проектирования, который определяет интерфейс для создания объектов, но позволяет подклассам выбирать классы для создания. То есть, данный шаблон делегирует создание объектов наследникам родительского класса.

Рассмотрим пример использования фабричного метода:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

factory = AnimalFactory()
animal = factory.get_animal("dog")
print(animal.speak())  # выводит "Woof"
```

В данном примере определяется абстрактный класс `Animal`, содержащий абстрактный метод `speak()`. Затем определяются два подкласса `Dog` и `Cat`, которые реализуют метод `speak()`.

Кроме того, определяется класс `AnimalFactory`, который содержит метод `get_animal()`, который создает объекты классов `Dog` и `Cat` в зависимости от аргумента `animal_type`.

2. Абстрактная фабрика (Abstract Factory) - это порождающий шаблон проектирования, который предоставляет интерфейс для создания семейств связанных или зависимых объектов без указания конкретных классов.

Рассмотрим пример использования абстрактной фабрики:

```python
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class MacOSButton(Button):
    def paint(self):
        return "Render a button in a Mac OS style"

class WindowsButton(Button):
    def paint(self):
        return "Render a button in a Windows style"

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class MacOSCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in a Mac OS style"

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Render a checkbox in a Windows style"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

factory = MacOSfactory = MacOSFactory()

button = factory.create_button()
checkbox = factory.create_checkbox()

print(button.paint())     # выводит "Render a button in a Mac OS style"
print(checkbox.paint())   # выводит "Render a checkbox in a Mac OS style"
```

В данном примере определяется абстрактный класс `Button` и его два подкласса `MacOSButton` и `WindowsButton`, а также абстрактный класс `Checkbox` и его два подкласса `MacOSCheckbox` и `WindowsCheckbox`.

Далее определяется абстрактная фабрика `GUIFactory`, содержащая методы `create_button()` и `create_checkbox()`, которые создают кнопки и флажки соответственно.

Затем определяются две конкретные фабрики `MacOSFactory` и `WindowsFactory`, каждая из которых реализует методы `create_button()` и `create_checkbox()` для создания соответствующих элементов GUI в соответствии с определенным стилем операционной системы.

Наконец, создается объект фабрики `MacOSFactory`, который используется для создания объектов `MacOSButton` и `MacOSCheckbox`.

Таким образом, абстрактная фабрика позволяет создавать семейства объектов, связанных друг с другом, не зависящих от конкретных классов, что обеспечивает более гибкую структуру приложения и упрощает его расширение.

3. Строитель (Builder) - это порождающий шаблон проектирования, который используется для поэтапного создания сложных объектов, позволяя использовать различные способы конфигурации.

Рассмотрим пример использования шаблона проектирования "Строитель":

```python
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.create_new_car()
        self.builder.add_model()
        self.builder.add_tires()
        self.builder.add_engine()

    def get_car(self):
        return self.builder.car

class Builder:
    def __init__(self):
        self.car = None

    def create_new_car(self):
        self.car = Car()

class FerrariBuilder(Builder):
    def add_model(self):
        self.car.model = "Ferrari"

    def add_tires(self):
        self.car.tires = "Pirelli"

    def add_engine(self):
        self.car.engine = "V8"

class Car:
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return f"{self.model} | {self.tires} | {self.engine}"

builder = FerrariBuilder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)  # выводит "Ferrari | Pirelli | V8"
```

В данном примере определяется класс `Director`, который координирует процесс поэтапного создания сложных объектов.

Далее определяется абстрактный класс `Builder`, который предоставляет интерфейс для создания различных частей сложного объекта, а также его подкласс `FerrariBuilder`, который реализует методы для создания объекта класса `Car` с конкретной конфигурацией.

Класс `Car` представляет собой сложный объект, который создается поэтапно с помощью объекта `Director` и конкретного `Builder`.

Таким образом, шаблон проектирования "Строитель" позволяет создавать сложные объекты поэтапно, при этом предоставляя возможность использовать различные конфигурации и изменять процесс создания объекта без изменения самого объекта.

В целом, порождающие шаблоны проектирования позволяют более гибко управлять процессом создания объектов, улучшить модульность кода и повторно использовать его компоненты.

## Структурные шаблоны
Структурные шаблоны проектирования (structural patterns) используются для объединения классов и объектов в более крупные структуры. Некоторые из наиболее распространенных структурных шаблонов проектирования в Python:

1. Адаптер (Adapter) - это структурный шаблон проектирования, который позволяет использовать уже существующий класс с другим интерфейсом без изменения его исходного кода.

Рассмотрим пример использования шаблона проектирования "Адаптер":

```python
class LegacyRectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def legacy_draw(self):
        print(f"Legacy rectangle: ({self.x1},{self.y1}),({self.x2},{self.y2})")

class RectangleAdapter:
    def __init__(self, x, y, width, height):
        self.rectangle = LegacyRectangle(x, y, x + width, y + height)

    def draw(self):
        self.rectangle.legacy_draw()

adapter = RectangleAdapter(10, 10, 100, 200)
adapter.draw()  # выводит "Legacy rectangle: (10,10),(110,210)"
```

В данном примере определяется класс `LegacyRectangle`, который представляет собой уже существующий класс, имеющий свой интерфейс и метод `legacy_draw()`, который рисует прямоугольник.

Затем определяется класс `RectangleAdapter`, который использует объект класса `LegacyRectangle` и адаптирует его интерфейс под интерфейс `draw()`. Класс `RectangleAdapter` создает объект класса `LegacyRectangle` в конструкторе и переопределяет метод `draw()`, который в свою очередь вызывает метод `legacy_draw()` у объекта класса `LegacyRectangle`.

Таким образом, класс `RectangleAdapter` предоставляет клиентам единый интерфейс `draw()`, который адаптирован для использования уже существующего класса `LegacyRectangle`.

2. Мост (Bridge) - это структурный шаблон проектирования, который разделяет абстракцию и ее реализацию, позволяя их изменять независимо друг от друга.

Рассмотрим пример использования шаблона проектирования "Мост":

```python
class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at ({x}, {y}) with radius {radius}")

class DrawingAPI2:
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at ({x}, {y}) with radius {radius}")

class CircleShape:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent

circle1 = CircleShape(1, 2, 3, DrawingAPI1())
circle2 = CircleShape(4, 5, 6, DrawingAPI2())

circle1.draw()  # выводит "API1.circle at (1, 2) with radius 3"
circle2.draw()  # выводит "API2.circle at (4, 5) with radius 6"

circle1.scale(2)
circle2.scale(3)

circle1.draw()  # выводит "API1.circle at (1, 2) with radius 6"
circle2.draw()  # выводит "API2.circle at (4, 5) with radius 18"
```

В данном примере определяются две реализации `DrawingAPI1` и `DrawingAPI2`, которые представляют собой разные способы рисования окружности.

Далее определяется абстракция `CircleShape`, которая имеет свойство `_drawing_api` типа `DrawingAPI` и методы `draw()` и `scale()`. Метод `draw()` использует метод `draw_circle()` у объекта `_drawing_api` для рисования окружности, а метод `scale()` изменяет радиус окружности.

Наконец, создаются два объекта `CircleShape` с разными параметрами и разными объектами `DrawingAPI`. Методы `draw()` и `scale()` вызываются у каждого объекта, демонстрируя возможность использования разных реализаций `DrawingAPI` с одной абстракцией `CircleShape`.

3. Компоновщик (Composite) - это структурный шаблон проектирования, который позволяет объединять объекты в древовидную структуру и работать с этой структурой так, как будто это единичный объект.

Рассмотрим пример использования шаблона проектирования "Компоновщик":

```python
class Component:
    def __init__(self, name):
        self._name = name

    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return f"Leaf {self._name} operation"

class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Composite {self._name} operation with {', '.join(results)}"

leaf1 = Leaf("1")
leaf2 = Leaf("2")
leaf3 = Leaf("3")
leaf4 = Leaf("4")

composite1 = Composite("A")
composite1.add(leaf1)
composite1.add(leaf2)

composite2 = Composite("B")
composite2.add(leaf3)
composite2.add(leaf4)

composite1.add(composite2)

print(leaf1.operation())        # выводит "Leaf 1 operation"
print(composite1.operation())  # выводит "Composite A operation with Leaf 1 operation..."
```

В данном примере определяется класс `Component`, который представляет собой общий интерфейс для всех объектов, включая листья и контейнеры. Класс `Leaf` представляет собой листовой объект, а класс `Composite` - контейнер, который может содержать другие объекты типа `Component`.

Класс `Composite` имеет методы `add()` и `remove()` для добавления и удаления объектов в контейнере, а метод `operation()` вызывает метод `operation()` для каждого объекта в контейнере и возвращает результат их работы.

Наконец, создаются несколько объектов `Leaf` и `Composite`, которые добавляются друг к другу в различные комбинации. Метод `operation()` вызывается у каждого объекта, демонстрируя возможность работы с древовидной структурой объектов как с единичным объектом.

4. Приспособленец (Flyweight) - это структурный шаблон проектирования, который позволяет эффективно поддерживать большое количество мелких объектов.

Рассмотрим пример использования шаблона проектирования "Приспособленец":

```python
class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        return f"Flyweight with shared state {self._shared_state} and unique state {unique_state}"

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]

factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("shared state")
flyweight2 = factory.get_flyweight("shared state")

print(flyweight1.operation("unique state"))  # выводит "Flyweight with shared state shared state and unique state unique state"
print(flyweight2.operation("different unique state"))  # выводит "Flyweight with shared state shared state and unique state different unique state"
```

В данном примере определяются классы `Flyweight` и `FlyweightFactory`. Класс `Flyweight` представляет собой легковесный объект, который имеет общее состояние `_shared_state` и уникальное состояние, передаваемое в метод `operation()`.

Класс `FlyweightFactory` предоставляет метод `get_flyweight()`, который возвращает объект класса `Flyweight` с заданным общим состоянием. Если объект с указанным состоянием уже создан, метод `get_flyweight()` возвращает его из кэша, иначе создает новый объект.

Наконец, создаются два объекта `Flyweight` с одинаковым общим состоянием, и метод `operation()` вызывается для каждого объекта, демонстрируя возможность использования легковесных объектов для поддержки большого количества мелких объектов.

5. Заместитель (Proxy) - это структурный шаблон проектирования, который позволяет создавать объект-заместитель для другого объекта, который может управлять доступом к нему и добавлять дополнительную функциональность.

Рассмотрим пример использования шаблона проектирования "Заместитель":

```python
class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject request"

class Proxy(Subject):
    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        if self.check_access():
            return self._real_subject.request()
        else:
            return "Proxy: Access denied"

    def check_access(self):
        return False

class AuthorizedProxy(Proxy):
    def check_access(self):
        return True

subject = AuthorizedProxy()
print(subject.request())  # выводит "RealSubject request"
```

В данном примере определяются классы `Subject`, `RealSubject`, `Proxy` и `AuthorizedProxy`. Класс `Subject` представляет собой общий интерфейс для реального объекта и его заместителя. Класс `RealSubject` представляет собой реальный объект, который выполняет операцию `request()`.

Класс `Proxy` представляет собой объект-заместитель для `RealSubject`. Он имеет ссылку на реальный объект `_real_subject` и реализует метод `request()`, который проверяет доступ к реальному объекту перед выполнением операции.

Класс `AuthorizedProxy` представляет собой заместителя с авторизацией, который всегда возвращает `True` из метода `check_access()`, что позволяет использовать реальный объект без проверки доступа.

Наконец, создается объект `AuthorizedProxy`, и метод `request()` вызывается у него, демонстрируя возможность использования заместителя для реального объекта с контролем доступа.

## поведенческие шаблоны

Поведенческие шаблоны проектирования определяют взаимодействие между объектами и обеспечивают более гибкую и эффективную организацию кода. Ниже приведены некоторые примеры поведенческих шаблонов проектирования в Python:

1. Стратегия (Strategy) - это поведенческий шаблон проектирования, который позволяет выбирать алгоритм во время выполнения программы.

Рассмотрим пример использования шаблона проектирования "Стратегия":

```python
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute(self):
        return self._strategy.execute()

class Strategy:
    def execute(self):
        pass

class ConcreteStrategy1(Strategy):
    def execute(self):
        return "ConcreteStrategy1 execute"

class ConcreteStrategy2(Strategy):
    def execute(self):
        return "ConcreteStrategy2 execute"

context1 = Context(ConcreteStrategy1())
print(context1.execute())  # выводит "ConcreteStrategy1 execute"

context2 = Context(ConcreteStrategy2())
print(context2.execute())  # выводит "ConcreteStrategy2 execute"
```

В данном примере определяются классы `Context`, `Strategy`, `ConcreteStrategy1` и `ConcreteStrategy2`. Класс `Context` использует объект класса `Strategy` для выполнения операции `execute()`.

Класс `Strategy` представляет собой интерфейс для всех поддерживаемых алгоритмов, а классы `ConcreteStrategy1` и `ConcreteStrategy2` представляют конкретные реализации этих алгоритмов.

Наконец, создаются объекты `Context` с разными объектами `Strategy`, и метод `execute()` вызывается у каждого объекта, демонстрируя возможность выбора алгоритма во время выполнения программы.

2. Наблюдатель (Observer) - это поведенческий шаблон проектирования, который позволяет оповещать объекты об изменениях в других объектах.

Рассмотрим пример использования шаблона проектирования "Наблюдатель":

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        pass

class ConcreteObserver1(Observer):
    def update(self):
        print("ConcreteObserver1 update")

class ConcreteObserver2(Observer):
    def update(self):
        print("ConcreteObserver2 update")

subject = Subject()
observer1 = ConcreteObserver1()
observer2 = ConcreteObserver2()

subject.attach(observer1)
subject.attach(observer2)

subject.notify()  # выводит "ConcreteObserver1 update" и "ConcreteObserver2 update"

subject.detach(observer2)

subject.notify()  # выводит "ConcreteObserver1 update"
```

В данном примере определяются классы `Subject`, `Observer`, `ConcreteObserver1` и `ConcreteObserver2`. Класс `Subject` представляет собой объект-издатель, у которого есть список наблюдателей (`_observers`), которые должны быть уведомлены об изменении состояния объекта-издателя.

Класс `Observer` представляет собой интерфейс для всех объектов-наблюдателей, а классы `ConcreteObserver1` и `ConcreteObserver2` представляют конкретные реализации объектов-наблюдателей.

Когда происходит изменение состояния объекта-издателя (`subject`), вызывается метод `notify()`, который уведомляет всех наблюдателей о изменении. Каждый наблюдатель, подписанный на изменения объекта-издателя, получает уведомление в своем методе `update()`, который затем может выполнить соответствующие действия.

3. Команда (Command) - это поведенческий шаблон проектирования, который позволяет инкапсулировать запрос в объект и передавать его в качестве параметра другому объекту.

Рассмотрим пример использования шаблона проектирования "Команда":

```python
class Receiver:
    def action(self):
        pass

class Command:
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        pass

class ConcreteCommand(Command):
    def execute(self):
        self._receiver.action()

class Invoker:
    def set_command(self, command):
        self._command = command

    def execute_command(self):
        self._command.execute()

receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker()
invoker.set_command(command)

invoker.execute_command()  # вызывает метод action() у объекта receiver
```

В данном примере определяются классы `Receiver`, `Command`, `ConcreteCommand` и `Invoker`. Класс `Receiver` представляет объект, который должен выполнить действие.

Класс `Command` представляет объект-команду, который инкапсулирует запрос в виде объекта. Класс `ConcreteCommand` представляет конкретную реализацию команды, которая вызывает метод `action()` у объекта `Receiver`.

Класс `Invoker` представляет объект, который выполняет команду. Он имеет метод `set_command()`, который принимает объект `Command` в качестве параметра, и метод `execute_command()`, который вызывает метод `execute()` у объекта `Command`.

Наконец, создается объект `Receiver`, объект `ConcreteCommand` с объектом `Receiver` в качестве параметра, объект `Invoker` и метод `set_command()` вызывается у него с объектом `ConcreteCommand`. Метод `execute_command()` вызывается у объекта `Invoker`, вызывая метод `execute()` у объекта `ConcreteCommand` и, в результате, метод `action()` у объекта `Receiver`.
