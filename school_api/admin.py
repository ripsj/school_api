from django.contrib import admin
from .models import Professor
from .models import Course
from .models import Lesson
from .models import Question
from .models import Answer
from .models import Student

# Register your models here.
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)