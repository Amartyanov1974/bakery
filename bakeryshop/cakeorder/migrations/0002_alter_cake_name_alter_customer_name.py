# Generated by Django 4.2.3 on 2023-07-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeorder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='name',
            field=models.CharField(blank=True, default='Торт', max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Имя клиента'),
        ),
    ]
