# Generated by Django 3.1.2 on 2020-10-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
