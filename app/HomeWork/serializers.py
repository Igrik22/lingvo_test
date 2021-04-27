from rest_framework import serializers
from .models import HomeWork, FinishedHomeWork
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

        
    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance


class HomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWork
        fields = ('id', 'title', 'work_text', 'home_work_file', 'comment', 'pub_date', 'faculty')


class FinishedHomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishedHomeWork
        fields = ('id', 'title', 'home_work', 'finished_home_work_file', 'created', 'mark', 'faculty')
