from rest_framework import serializers
from .models import HomeWork, FinishedHomeWork


class HomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = ('id', 'title', 'work_text', 'home_work_file', 'comment', 'pub_date', 'faculty', 'finished_date')


class FinishedHomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishedHomeWork
        fields = ('id', 'user', 'title', 'home_work', 'finished_home_work_file', 'created', 'mark', 'faculty')





