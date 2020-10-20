# Описание
API для проекта социальной сети YaTube, основанный на Django-Rest-Framework

Функционал включает в себя:
1) Авторизацию по JWT (JSON Web Token) токену
2) Сериализацию данных для всех моделей проекта (Post, Comment, Group, Follow)
3) Обработку GET, POST, PATCH, PUT и DELETE запросов к базе данных YaTube

# Установка и запуск на локальной машине
1. Склонировать репозиторий

2. Создать и активировать виртуальное окружение для проекта

```python -m venv venv```

unix консоль:

```source venv/scripts/activate```

windows консоль:

```venv/scripts/activate.bat```

3. Установить зависимости и сделать миграции

```
python pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

4. Запустить сервер

```python manage.py runserver```

# Примеры использования

* ##Получение токена авторизации
    ### Request
    ```
        POST /api/v1/token/
        form-data: {"username": "username_string", "password": "password_string"}
    ```
    ### Response
        {
          "refresh": "<JRW-refresh-token>",
          "access": "<JRW-access-token>",
        }

* ##Обновление токена
    ### Request
    ```
        POST /api/v1/token/refresh/
        form-data: {"refresh": "JRW-refresh-token"}
    ```
    ### Response
        {
          "access": "<new-JRW-access-token>"
        }

* ##Получение списка всех постов
    ### Request
    ```
        GET /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    ### Response
        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]

* ##Создание нового поста
    ### Request
    ```
        POST /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
    ```
    ### Response
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ##Получение поста по его id
    #### Request
    ```
        GET /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    #### Response
        status_code: 200
        {
            "id": <post_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ##Обновление поста по его id
    #### Request
    ```
        PUT /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    #### Response
        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ##Частичное обновление поста по его id
    #### Request
    ```
        PATCH /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    #### Response
        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
        
* ##Удаление поста по его id
    #### Request
    ```
        DELETE /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    #### Response
        status_code: 204
        
* ##Получение списка всех комментариев
    #### Request
    ```
        GET /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    #### Response
        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
        
* ##Создание нового комментария
    #### Request
    ```
        POST /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
    ```
    #### Response
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ##Получение комментария по его id
    #### Request
    ```
        POST /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    #### Response
        status_code: 200
        {
            "id": <comment_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ##Обновление комментария по его id
    #### Request
    ```
        PUT /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
    ```
    #### Response
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ##Частичное обновление комментария по его id
    #### Request
    ```
        PATCH /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
    ```
    #### Response
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ##Удаление комментария по его id
    #### Request
    ```
        DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    #### Response
        status_code: 204

* ##Получение списка всех подписчиков
    #### Request
    ```
        GET /api/v1/follow/?search={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    #### Response
        status_code: 200
        [
            {
                "user": "string",
                "following": "string"
            },
            ...
        ]

* ##Создание подписки
    #### Request
    ```
        POST /api/v1/follow/?user={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"following": "string"}
    ```
    #### Response
        status_code: 200
        {
            "user": "string",
            "following": "string"
        }

* ##Получение списка всех групп
    #### Request
    ```
        GET /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    #### Response
        status_code: 200
        [
            {
                "title": "string"
            },
            ...
        ]

* ##Создание новой группы
    #### Request
    ```
        POST /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"title": "string"}
    ```
    #### Response
        status_code: 200
        {
            "title": "string"
        }
