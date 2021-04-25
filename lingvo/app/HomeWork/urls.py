from django.urls import path
from HomeWork.views import HomeWorkAPIView, FinishedHomeWorkAPIView, RegisterView, LoginView

urlpatterns = [
    path('home-work/', HomeWorkAPIView.as_view(), name='Homework'),
    path('finished-home-work/', FinishedHomeWorkAPIView.as_view(), name='Finishedhomework'),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view())
]