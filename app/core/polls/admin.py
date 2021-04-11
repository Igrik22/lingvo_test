from django.contrib import admin

from django.contrib import admin
from .models import Question, Answer, Choice, TestTheme, TestQuestion, TestChoice, TestResult


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'visible',
        'max_points',
    )


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'title',
        'points',
        'lock_other',
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)

class TestThemeAdmin(admin.ModelAdmin):
    list_display = (
        'theme_name',
        'group',
    )
    list_filter = ('group',)


class TestQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'theme',
        'question',
    )

class TestChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'text_answer',
        'points',
        'lock_other',
    )


class TestResultAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user', 'question',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(TestTheme, TestThemeAdmin)
admin.site.register(TestQuestion, TestQuestionAdmin)
admin.site.register(TestChoice, TestChoiceAdmin)
admin.site.register(TestResult, TestResultAdmin)
