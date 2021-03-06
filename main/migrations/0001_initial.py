# Generated by Django 4.0.2 on 2022-03-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Название места')),
                ('byName', models.CharField(max_length=40, verbose_name='Автор')),
                ('byPhoto', models.ImageField(blank=True, null=True, upload_to='static/main/author/', verbose_name='by Фото')),
                ('money', models.CharField(max_length=10, verbose_name='Цена')),
                ('first', models.CharField(max_length=40, verbose_name='Особенность 1')),
                ('second', models.CharField(max_length=40, verbose_name='Особенность 2')),
                ('dateTime', models.DateTimeField(verbose_name='Дата')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/main/', verbose_name='Фото')),
            ],
        ),
    ]
