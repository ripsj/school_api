from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfessorSerializer
from .serializers import CourseSerializer
from .serializers import LessonSerializer
from .serializers import QuestionSerializer
from .serializers import AnswerSerializer
from .serializers import StudentSerializer
from .models import Professor
from .models import Course
from .models import Lesson
from .models import Question
from .models import Answer
from .models import Student


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all().order_by('name')
    serializer_class = ProfessorSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all().order_by('name')
    serializer_class = LessonSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('question')
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('answer')
    serializer_class = AnswerSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer