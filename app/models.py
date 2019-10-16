from django.db import models
from app import models as mod
# Create your models here.


class Planet(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название планеты')

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

    def __str__(self):
        return self.name


class Recruit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя рекрутера')
    planet = models.ForeignKey(mod.Planet, null=True, on_delete=models.SET_NULL, verbose_name='Планета обитания')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Адресс электронной почты')

    class Meta:
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'

    def __str__(self):
        return self.name


class Sith(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя ситха')
    planet = models.ForeignKey(mod.Planet, null=True, on_delete=models.SET_NULL,
                               verbose_name='Планета на которой он обучает')
    recruits = models.ManyToManyField(mod.Recruit, verbose_name='Список рекрутов')

    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=255, verbose_name='Вопрос')
    correct_answer = models.BooleanField(verbose_name="Правильный ответ", default=False)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.name


class TestTrials(models.Model):
    id_order = models.IntegerField(unique=True, verbose_name='Уникальный код ордена')
    questions = models.ManyToManyField(mod.Question, verbose_name='Список вопросов')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.id_orden


class QuestionAsk(models.Model):
    recruit = models.ForeignKey(mod.Recruit, verbose_name='Рекрут', on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(mod.Question, verbose_name='Вопрос', on_delete=models.SET_NULL, null=True)
    answer = models.BooleanField(verbose_name='Ответ рекрута', default=False)

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'

    def __str__(self):
        return "{0} - {1} : {2}".format(self.recruit, self.answer, self.question)
