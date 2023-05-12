Параллелизм (parallelism) в Python позволяет выполнять задачи параллельно на нескольких процессорных ядрах или в нескольких процессах. Это позволяет увеличить производительность программы за счет распределения работы между несколькими вычислительными ресурсами.

В Python для достижения параллелизма можно использовать многопроцессорность (multiprocessing) или сторонние библиотеки, такие как `concurrent.futures` и `mpi4py`. Рассмотрим примеры использования параллелизма в Python:

1. Многопроцессорность (multiprocessing):
```python
import multiprocessing

def process_data(data):
    # Обработка данных

data = [1, 2, 3, 4, 5]

# Создание пула из 4 процессов
pool = multiprocessing.Pool(processes=4)

# Применение функции к каждому элементу в списке data
results = pool.map(process_data, data)

# Завершение пула процессов
pool.close()
pool.join()

# Обработка результатов
for result in results:
    # Действия с результатами
```
В этом примере создается пул из 4 процессов с помощью `multiprocessing.Pool()`. Затем метод `map()` позволяет применить функцию `process_data` к каждому элементу в списке `data` параллельно, используя доступные процессорные ядра. Результаты возвращаются в виде списка `results`, который можно обработать по мере необходимости.

2. Библиотека concurrent.futures:
```python
from concurrent.futures import ProcessPoolExecutor

def process_data(data):
    # Обработка данных

data = [1, 2, 3, 4, 5]

# Создание пула из 4 процессов
with ProcessPoolExecutor(max_workers=4) as executor:
    # Отправка задачи на выполнение в пуле
    futures = [executor.submit(process_data, d) for d in data]

    # Получение результатов выполнения задач
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

# Обработка результатов
for result in results:
    # Действия с результатами
```
В этом примере используется `ProcessPoolExecutor` из `concurrent.futures` для создания пула из 4 процессов. Затем задача `process_data` отправляется на выполнение в пуле с помощью `executor.submit()`, и результаты выполнения задач получаются с использованием `concurrent.futures.as_completed()`. Результаты могут быть обработаны по мере необходимости.
