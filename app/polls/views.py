from .serializers import QuestionSerializer, AnswerSerializer, TestThemeSerializer, TestResultSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Question, TestTheme, TestResult


class GetQuestion(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.filter(visible=True, )

    def get(self, request, format=None):
        questions = Question.objects.filter(visible=True, )
        last_point = QuestionSerializer(questions, many=True)
        print(last_point.data)
        return Response(last_point.data)


class QuestionAnswer(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AnswerSerializer

    def post(self, request, format=None):
        answer = AnswerSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})


class GetTestTheme(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TestThemeSerializer
    queryset = TestTheme.objects.all()

    def get(self, request, format=None):
        test_theme = TestTheme.objects.all()
        serializer = TestThemeSerializer(test_theme, many=True)
        return Response(serializer.data)


class GetTestResult(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TestResult.objects.all()

    def get(self, request, format=None):
        test_result = TestResult.objects.all()
        serializer = TestResultSerializer(test_result, many=True)
        return Response(serializer.data)
