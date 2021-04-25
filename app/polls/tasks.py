from celery import shared_task, Celery
from .models import TestTheme
import random
import string


# @shared_task
# def test_date():
#     test_themes = TestTheme.objects.all()
#     for test_theme in test_themes:
#         if test_theme.deadline_check:
#             test_theme.test_active = True
#             test_theme.save()
#         else:
#             test_theme.test_active = False
#             test_theme.save()
from lingvo_3.celery import app


@app.task
def test_date():
    test_themes = TestTheme.objects.all()
    for test_theme in test_themes:
        if test_theme.deadline_check:
            test_theme.test_active = True
            test_theme.save()
        else:
            test_theme.test_active = False
            test_theme.save()