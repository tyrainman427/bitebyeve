# Generated by Django 3.1.2 on 2020-11-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201115_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Pending', 'Pending'), ('Out For Delivery', 'Out For Delivery'), ('Ready For Pick Up', 'Ready For Pick Up')], default='Created', max_length=20, null=True),
        ),
    ]
