# Generated by Django 3.1.2 on 2020-10-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('Meal 1', 'Meal 1'), ('Meal 2', 'Meal 2'), ('Meal 3', 'Meal 3'), ('Meal 4', 'Meal 4')], max_length=50),
        ),
    ]
