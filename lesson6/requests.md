## requests
```
pip install requests
```

Requests - это библиотека для работы с HTTP-запросами в Python. Она предоставляет простой и удобный интерфейс для отправки запросов на сервер и получения ответов. Эта библиотека включает в себя множество методов и параметров, которые позволяют настраивать запросы и обрабатывать ответы.

Примеры методов:
- `requests.get(url, params=None, **kwargs)` - отправляет GET-запрос на указанный URL-адрес с параметрами запроса.
- `requests.post(url, data=None, json=None, **kwargs)` - отправляет POST-запрос на указанный URL-адрес с данными запроса в теле сообщения.
- `requests.put(url, data=None, **kwargs)` - отправляет PUT-запрос на указанный URL-адрес с данными запроса в теле сообщения.
- `requests.delete(url, **kwargs)` - отправляет DELETE-запрос на указанный URL-адрес.
- `requests.head(url, **kwargs)` - отправляет HEAD-запрос на указанный URL-адрес.

Каждый из этих методов возвращает объект `Response`, который содержит ответ от сервера. В объекте `Response` можно получить различные данные, такие как статус-код, заголовки ответа, содержимое ответа и другие.

Примеры параметров:
- `params` - словарь параметров запроса, который будет добавлен в URL-адрес.
- `data` - данные запроса в виде словаря, который будет отправлен в теле сообщения вместе с запросом.
- `json` - данные запроса в формате JSON, который будет отправлен в теле сообщения вместе с запросом.
- `headers` - заголовки запроса в виде словаря.
- `cookies` - куки, которые нужно отправить с запросом.
- `auth` - объект класса `HTTPBasicAuth`, `HTTPDigestAuth` или другого класса, который предоставляет данные для авторизации.
- `timeout` - максимальное время ожидания ответа от сервера.
- `allow_redirects` - указывает, должен ли запрос следовать перенаправлениям.

Библиотека Requests также предоставляет возможность работать с сессиями и сокращает код для отправки повторяющихся запросов. Сессии позволяют сохранять данные между запросами, такие как авторизационные данные или cookie.


Пример использования библиотеки requests для отправки GET-запроса:

```
import requests

response = requests.get('https://www.example.com')

print(response.text)
```

В данном примере мы отправляем GET-запрос на сайт example.com и выводим полученный от сервера текст. Библиотека requests автоматически устанавливает соединение с сервером, отправляет запрос и получает ответ.

Кроме того, библиотека requests предоставляет множество дополнительных функций, таких как сессии, управление cookie, обработка исключений и многое другое. Это позволяет еще более удобно работать с HTTP-запросами и улучшить производительность вашего кода.


Библиотека Requests предоставляет простой и удобный интерфейс для работы с HTTP-запросами в Python. Вот несколько наиболее распространенных методов и параметров этой библиотеки:

1. Метод GET: используется для получения информации с сервера. Пример:

```
import requests

response = requests.get('https://www.example.com')
print(response.text)
```

2. Метод POST: используется для отправки данных на сервер, например, для создания нового ресурса. Пример:

```
import requests

data = {'username': 'user', 'password': 'pass'}
response = requests.post('https://www.example.com/login', data=data)
print(response.status_code)
```

3. Метод PUT: используется для обновления существующего ресурса на сервере. Пример:

```
import requests

data = {'name': 'new name', 'age': 25}
response = requests.put('https://www.example.com/profile', data=data)
print(response.status_code)
```

4. Метод DELETE: используется для удаления ресурса на сервере. Пример:

```
import requests

response = requests.delete('https://www.example.com/item/1')
print(response.status_code)
```

5. Параметр params: используется для передачи параметров в запросе. Пример:

```
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://www.example.com/get', params=payload)
print(response.url)
```

6. Параметр headers: используется для отправки заголовков в запросе. Пример:

```
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://www.example.com', headers=headers)
print(response.status_code)
```

7. Параметр cookies: используется для передачи cookie в запросе. Пример:

```
import requests

cookies = {'session_id': '123'}
response = requests.get('https://www.example.com', cookies=cookies)
print(response.status_code)
```

8. Параметр timeout: используется для установки времени ожидания ответа от сервера. Пример:

```
import requests

response = requests.get('https://www.example.com', timeout=5)
print(response.status_code)
```


Атрибут `content` возвращает содержимое ответа в виде байтов. Этот атрибут полезен, когда необходимо получить содержимое в бинарном формате, например, для сохранения в файл или передачи по сети. Например, чтобы получить содержимое в виде байтов, можно использовать следующий код:

```
import requests

response = requests.get('https://www.example.com')
content = response.content
print(content)
```

Важно помнить, что использование атрибута `content` может потребовать дополнительной обработки, например, если содержимое ответа является изображением или другим бинарным файлом. В таком случае необходимо сохранить содержимое в файл или передать его в соответствующий обработчик.
