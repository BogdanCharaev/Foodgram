from django.core.validators import MinValueValidator
from django.db import models
from foodgram.settings import MIN_VALUE_AMOUNT, MIN_VALUE_COOKING_TIME
from users.models import User


class Tag(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название тэга'
    )
    color = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Цветовой HEX-код'
    )
    slug = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Слаг'
    )

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.slug


class Ingredient(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название ингредиента'
    )
    measurement_unit = models.CharField(
        max_length=30,
        verbose_name='Единицы измерения'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор публикации'
    )
    name = models.CharField(
        max_length=254,
        verbose_name='Название'
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='Картинка',
    )
    text = models.TextField(
        verbose_name='Текстовое описание'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='AmountOfIngredient',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тэг'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        validators=(
            MinValueValidator(
                MIN_VALUE_COOKING_TIME,
                message=(f'Время приготовления не может быть меньше'
                         f'{MIN_VALUE_COOKING_TIME}')
            ),
        )
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class AmountOfIngredient(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='recipe_ingredients'
    )
    amount = models.IntegerField(
        verbose_name='Количество ингредиента',
        validators=(
            MinValueValidator(
                MIN_VALUE_AMOUNT,
                message=(f'Количество ингредиента не может быть меньше '
                         f'{MIN_VALUE_AMOUNT}')
            ),
        ))

    class Meta:
        ordering = ('id',)
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='favorite_recipes', verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='users', verbose_name='Рецепт'
    )

    class Meta:
        ordering = ('user',)
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_user_recipe_favorite'
            ),
        )
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='shopping_carts', verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='shopping_carts', verbose_name='Рецепт'
    )

    class Meta:
        ordering = ('user',)
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_user_recipe_shopping_cart'
            ),
        )
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
