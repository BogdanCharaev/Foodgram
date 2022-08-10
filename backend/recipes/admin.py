from django.contrib import admin
from recipes.models import (AmountOfIngredient, Favorite, Ingredient, Recipe,
                            ShoppingCart, Tag)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('measurement_unit',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author',)
    search_fields = ('name', 'author__username', 'author__email')
    list_filter = ('author', 'name', 'tags')


@admin.register(AmountOfIngredient)
class AmountOfIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount')
    search_fields = (
        'recipe__name',
        'ingredient__name',
        'recipe__author__username',
        'recipe__author__email'
    )
    list_filter = ('recipe__tags',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe',)
    search_fields = ('recipe__name', 'user__username', 'user__email')
    list_filter = ('recipe__tags',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_dislay = ('id', 'user', 'recipe')
    search_fields = ('recipe__name', 'user__username', 'user__email')
    list_filter = ('recipe__tags',)
