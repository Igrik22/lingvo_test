from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from . import models
from .serializers import HomeWorkSerializer, FinishedHomeWorkSerializer, UserSerializer
from rest_framework.response import Response


class RegisterView(APIView):

    def post(self, request):
        # serializer = UserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        print(request.data)
        user, _ = models.User.objects.get_or_create(**request.data)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class HomeWorkAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = HomeWorkSerializer

    def get(self, request):
        queryset = models.HomeWork.objects.all()
        serializer = HomeWorkSerializer(queryset, many=True)
        return Response(serializer.data)


class FinishedHomeWorkAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FinishedHomeWorkSerializer

    def get(self, request):
        queryset = models.FinishedHomeWork.objects.all()
        serializer = FinishedHomeWorkSerializer(queryset, many=True)
        return Response(serializer.data)
