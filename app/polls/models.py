from django.db import models
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User, Group
from lingvo_3 import settings
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

#----------------------------------------------------------------------

class Question(models.Model):
    title = models.CharField(max_length=4096)
    visible = models.BooleanField(default=False)
    max_points = models.FloatField()

    def __str__(self):
           return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)
    points = models.FloatField()
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(settings.USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.title

# ---------------------------------------------------------------------


class TestTheme(models.Model):
    theme_name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group")
    final_date = models.DateTimeField(default=None)
    test_active = models.BooleanField()

    def __str__(self):
        return self.theme_name

    @property
    def deadline_check(self):
        from django.utils import timezone
        if self.final_date > timezone.datetime.today():
            print('Тест активен')
            return True
        else:
            print('Срок прохождения теста истек')
            return False


class TestQuestion(models.Model):
    theme = models.ForeignKey(TestTheme, on_delete=models.DO_NOTHING)
    question = models.CharField('Текст вопроса', max_length=150)

    def __str__(self):
        return self.question


class TestChoice(models.Model):
    question = models.ForeignKey(TestQuestion, on_delete=models.DO_NOTHING)
    text_answer = models.CharField(max_length=255)
    points = models.BooleanField()
    lock_other = models.BooleanField(default=False)

    def __str__(self):
        return self.text_answer


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    choice = models.ForeignKey(TestChoice, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice.text_answer