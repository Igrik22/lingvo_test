from django.urls import path
from HomeWork.views import HomeWorkAPIView, FinishedHomeWorkAPIView


urlpatterns = [
    path('home-work/', HomeWorkAPIView.as_view(), name='Homework'),
    path('finished-home-work/', FinishedHomeWorkAPIView.as_view(), name='Finishedhomework'),
]