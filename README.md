### API для публикации постов с возможностью подписки на авторов.

### Примеры запросов:

your_host_ip - default 127.0.0.1:8000
Регистрация:
```
POST http://{your_host_ip}/api/v1/auth/signup/
{
    "username": "myuser",
    "password": "mypassword"
}
```

Вывод списка публикаций:
```
GET http://{your_host_ip}/api/v1/posts/
```

Создание публикации:
```
POST http://{your_host_ip}/api/v1/posts/
{
    "text": "This is my first post",
    "image": "string",
    "group": 0
}
```

Получение комментариев публикации.
```
GET http://{your_host_ip}/api/v1/posts/{post_id}/comments/

[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

Получение списка сообществ:
```
GET http://{your_host_ip}/api/v1/groups/
[
  {
    "id": 0,
    "title": "Group Title",
    "slug": "string",
    "description": "string"
  }
]
```

Подписаться на автора(Только для авторизованных пользователей):
```
POST http://{your_host_ip}/api/v1/follow/
{
    "following": "Username"
}
```

Получить список своих подписок(Только для авторизованных пользователей):
```
GET http://{your_host_ip}/api/v1/follow/
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/sokolovados/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Стэк:

Python 3.8<br>
Django 2.2<br>
Django Rest Framework 3.11<br>
DRF simplejwt 4.7<br>

### Автор
Вадим Соколов https://github.com/sokolovados
Максим Волочковский https://github.com/VarrySPb
Данил Воронин https://github.com/Bogdan-Malina

