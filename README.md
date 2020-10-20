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

* Получение токена авторизации
  POST: localhost:8000/token {"username": "username_string", "password": "password_string"}
  Response:
    {
      "access": "<JRW-access-token>",
      "refresh": "<JRW-refresh-token>"
    }
  
  
  
  
  
  
