from django.db import models
from app import models as mod
# Create your models here.


class Recruit(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя рекрутера')
    planet = models.CharField(max_length=255, verbose_name='Планета обитания', default='null')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Адресс электронной почты')
    is_shadow_hands = models.BooleanField(verbose_name='Рука тени', default=False)

    class Meta:
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'

    def __str__(self):
        return self.name


class Sith(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя ситха')
    planet = models.CharField(max_length=255, verbose_name='Планета обитания', default='null')

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
    id_order = models.IntegerField(unique=True, primary_key=True, verbose_name='Уникальный код ордена')
    questions = models.ManyToManyField(mod.Question, verbose_name='Список вопросов')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.id_order.__str__()


class QuestionAsk(models.Model):
    recruit = models.ForeignKey(mod.Recruit, verbose_name='Рекрут', on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(mod.Question, verbose_name='Вопрос', on_delete=models.SET_NULL, null=True)
    answer = models.CharField(max_length=255, verbose_name='Ответ рекрута', default="")

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'

    def __str__(self):
        return "{0} - {1} : {2}".format(self.recruit, self.answer, self.question)
