from HomeWork.models import FinishedHomeWork, HomeWork, User
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    search_fields = ('username',)


@admin.register(HomeWork)
class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'work_text', 'home_work_file', 'comment', 'pub_date', 'faculty', 'finished_date')
    search_fields = ('title',)


@admin.register(FinishedHomeWork)
class FinishedHomeWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'home_work', 'finished_home_work_file', 'created', 'user', 'mark',
                    'comment_of_mark', 'faculty')
    search_fields = ('title',)


