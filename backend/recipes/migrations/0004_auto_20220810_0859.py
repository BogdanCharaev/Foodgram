# Generated by Django 3.2.6 on 2022-08-10 05:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20220729_1624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amountofingredient',
            options={'ordering': ('id',), 'verbose_name': 'Количество ингредиента', 'verbose_name_plural': 'Количество ингредиентов'},
        ),
        migrations.AlterField(
            model_name='amountofingredient',
            name='amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Количество ингредиента не может быть меньше 1')], verbose_name='Количество ингредиента'),
        ),
        migrations.AlterField(
            model_name='amountofingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredients', to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Время приготовления не может быть меньше1')], verbose_name='Время приготовления в минутах'),
        ),
    ]
