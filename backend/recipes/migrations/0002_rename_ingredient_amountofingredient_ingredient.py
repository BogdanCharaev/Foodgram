# Generated by Django 3.2.14 on 2022-07-27 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amountofingredient',
            old_name='Ingredient',
            new_name='ingredient',
        ),
    ]
