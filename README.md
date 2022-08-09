![example workflow](https://github.com/BogdanCharaev/foodgram-project-react/actions/workflows/main.yml/badge.svg)
# Foodgram продуктовый помощник.  

## Описание.  


На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Установка на Ubuntu

Для запуска проекта нужно собрать и запустить контейнер из образа. Для этого нужно установить сам докер с плагином docker-compose:

    sudo apt install curl
    
    curl -fsSL https://get.docker.com -o get-docker.sh
    
    sh get-docker.sh
    
    sudo apt install docker-ce docker-compose -y  

Впишите ip своего сервера в конфигурационный файл infra/nginx.conf:  


Далее нужно скопировать через scp два файла конфигурации из папки infra на ваш сервер

    scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
    scp nginx.conf <username>@<host>:/home/<username>/nginx.conf  


Далее нужно создать и заполнить .env файл, который хранит учетные данные. Это делается для того чтобы не заливать пароли и секретные ключи в публичный доступ
.env файл выглядит так:

    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=<имя базы данных postgres>
    DB_USER=пользователь бд
    DB_PASSWORD=пароль
    DB_HOST=db
    DB_PORT=5432
    SECRET_KEY=секретный ключ проекта django

Воркфлоу может сам создать .env файл, но для этого нужно в секретах репозитория указать значения следующих ключей:

    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=имя базы данных postgres
    DB_USER=пользователь бд
    DB_PASSWORD=пароль
    DB_HOST=db
    DB_PORT=5432
    SECRET_KEY=секретный ключ django

Для того чтобы запулить образ в докер хаб воркфлоу необходимы учетные данные аккаунта докер хаба, так же через секреты:

    DOCKER_PASSWORD=<пароль от DockerHub>
    DOCKER_USERNAME=<имя пользователя>

Это данные для подключения к вашему серверу:  

    USER=username
    HOST=IP
    PASSPHRASE=пароль, если есть
    SSH_KEY=ssh ключ

Тг бот может отправлять сообщение на указанный id, после того как воркфлоу выполнен:  

    TELEGRAM_TO=ID чата получается через userinfobot
    TELEGRAM_TOKEN=Токен вашего бота у BotFather
