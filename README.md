## Aiogram-Django-Template (PostgreSQL)

----
#### Инструкция по установке

- Настраиваем файл ``.env`` по примеру ``.env_ex`` 
- Переходим в папку ``backend``
- Делаем настройки `python manage.py makemigrations main` & `python manage.py migrate` & `python manage.py createsuperuser` 
- После запускаем сайт `python manage.py runserver`
- Заходим на сайт и добавляем токен бота и администратора (Пункт обязателен к заполнению)
- Настраиваем Redis по [этой ссылке](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-20-04-ru)
- Запускаем `app.py` для запуска бота