# Generated by Django 2.2.6 on 2019-10-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionask',
            name='answer',
            field=models.CharField(default='', max_length=255, verbose_name='Ответ рекрута'),
        ),
    ]