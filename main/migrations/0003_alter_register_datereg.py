# Generated by Django 4.0.2 on 2022-04-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='dateReg',
            field=models.DateTimeField(verbose_name='Дата рождения'),
        ),
    ]
