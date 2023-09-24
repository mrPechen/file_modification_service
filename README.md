# File modification service.

API сервис для изменения загруженных файлов.

Запуск:
- Клонировать проект.
- В папке "file_handler" убрать расширение "txt" в файле ".env.txt" и указать данные для работы PostgreSQL и RabbitMQ.
- Из корня проекта запустить комманду "docker-compose up --build".


Описание:
- Подробное описание находится ниже в пункте "ТЗ".
- В сервисе доступно 2 эдпоинта:<br/>
  http://0.0.0.0:8000/api/v1/upload - POST запрос. На вход принимает тип "File" в формате {"file": filename.png/txt} (в postman в body указать тип "file", key = "file"). Эндпоинт переделывает любые ихображения в ЧБ и добавляет к файлу с раширением "txt" новую строку с предложением. Возвращает id файла, путь к файлу и логическое поле обработан ли файл.<br/>
  http://0.0.0.0:8000/api/v1/files - GET запрос. Возвращает список всех файлов.
- По адресу http://0.0.0.0:5555 можно посмотреть задачи Celery при помощи Flower.
- Так как в ТЗ не было указано что делать с обработанными файлами я их сохраняю в "file_handler/api/files/processed".
  
ТЗ:

![ALT TEXT](https://github.com/mrPechen/file_modification_service/blob/main/%D1%82%D0%B7.png)
