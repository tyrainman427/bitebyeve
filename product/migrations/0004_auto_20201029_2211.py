# Generated by Django 3.1.2 on 2020-10-29 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20201029_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_on',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]