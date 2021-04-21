from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from . import models
from .serializers import HomeWorkSerializer, FinishedHomeWorkSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        })


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

