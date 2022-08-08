# Очередной продуктовый помощник. 
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







