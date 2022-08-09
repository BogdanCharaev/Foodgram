https://github.com/BogdanCharaev/foodgram-project-react/actions/workflows/main.yml/badge.svg
# Foodgram продуктовый помощник.  

## Описание.



## Установка на Ubuntu

Для запуска проекта нужно собрать и запустить контейнер из образа. Для этого нужно установить сам докер с плагином docker-compose:

    sudo apt install curl
    
    curl -fsSL https://get.docker.com -o get-docker.sh
    
    sh get-docker.sh
    
    sudo apt install docker-ce docker-compose -y  

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






Финальный проект на курсе Python - разработчик Яндекс Практикума(На самом деле оригинальное название задания просто продуктовый помощник, а не очередной продуктовый помощник).

Задание по дефолту это создать сервис на котором пользователь может оставить рецепт, подписываться на других оставителей рецептов и т п.  


Модель юзер переопределена(унаследована от абстрактюзер) для того чтобы пользователь мог логиниться по имейлу и паролю.  


У рецепта кроме всего прочего есть две связи многие-ко-многим и одна из этих связей реализована через другую таблицу, которая хранит количество ингредиента.
Поэтому использованы вложенные сериалайзеры и переопределены методы to_representation, create update validate и прочее.  


Пользователь может добавлять рецепт в избранное и в корзину покупок чтобы распечатать список покупок. Для этого на вьюсет рецепта добавлены методы через @action, ну и на удаление из избранного и корзины покупок через mapping.  


Для follow/unfollow и follow list написаны просто апи вью.  


Вся авторизация, выдача токенов, смена паролей и т п выполнена с djoser. Только использован drf authtoken, а не jwt.  


Минимально изменен page_size_query_param и пагинация стала кастомной.  


Скопирован и вставлен кастомный пермишен  IsAuthorOrReadOnly который на самом деле IsOwnerOrReadOnly.  


Есть достаточно SerializerMethodField, особенно в FollowListSerializer из users.serializers  


Установка на linux





