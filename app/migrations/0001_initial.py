# Generated by Django 2.2.6 on 2019-10-17 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('correct_answer', models.BooleanField(default=False, verbose_name='Правильный ответ')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя рекрутера')),
                ('planet', models.CharField(default='null', max_length=255, verbose_name='Планета обитания')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='Адресс электронной почты')),
            ],
            options={
                'verbose_name': 'Рекрут',
                'verbose_name_plural': 'Рекруты',
            },
        ),
        migrations.CreateModel(
            name='TestTrials',
            fields=[
                ('id_order', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Уникальный код ордена')),
                ('questions', models.ManyToManyField(to='app.Question', verbose_name='Список вопросов')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя ситха')),
                ('planet', models.CharField(default='null', max_length=255, verbose_name='Планета обитания')),
                ('recruits', models.ManyToManyField(to='app.Recruit', verbose_name='Список рекрутов')),
            ],
            options={
                'verbose_name': 'Ситх',
                'verbose_name_plural': 'Ситхи',
            },
        ),
        migrations.CreateModel(
            name='QuestionAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.BooleanField(default=False, verbose_name='Ответ рекрута')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Question', verbose_name='Вопрос')),
                ('recruit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Recruit', verbose_name='Рекрут')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
    ]
