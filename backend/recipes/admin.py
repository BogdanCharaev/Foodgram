from django.contrib import admin
from recipes.models import (AmountOfIngredient, Favorite, Ingredient, Recipe,
                            ShoppingCart, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    list_filter = ('measurement_unit',)
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author',)
    list_filter = ('author', 'name', 'tags')
    search_fields = ('name',)


@admin.register(AmountOfIngredient)
class AmountOfIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount')
    search_fields = (
        'recipe__name',
        'ingredient__name',
        'recipe__author__username',
        'recipe__author__email'
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe',)
    list_filter = ('recipe__tags',)
    search_fields = ('recipe__name', 'author__username', 'author__email')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_dislay = ('id', 'user', 'recipe')
