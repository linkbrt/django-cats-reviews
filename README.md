# django-cats-reviews
Python/Django project for test
Стек: Django/Rest Framework/Postgres
1. Документация Swagger: http://127.0.0.1:8000/swagger/
2. Документация Redoc: http://127.0.0.1:8000/redoc/

Для старта проекта :
- Создать файл .env по образу .env.template. Заполнить данными для бд
- Билд и запуск: sudo docker compose build && sudo docker compose up

По умолчанию при запуске docker контейнера генерируются тестовые данные. Чтобы это убрать, удалите строку `python manage.py start_factory` из *entrypoint.sh*
