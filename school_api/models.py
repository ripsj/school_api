from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=60)
    previousCourse = models.OneToOneField('Course',null = True, blank = True, on_delete = 'null')

    def __str__(self):
    	return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=60)
    previousLesson = models.OneToOneField('Lesson', null = True, blank = True, on_delete = 'null')
    course = models.ForeignKey(Course, on_delete = 'null')

    def __str__(self):
        return self.name

class Question(models.Model):
    question = models.CharField(max_length=60)
    lesson = models.ForeignKey(Lesson, on_delete = 'null')

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=60)
    question = models.ForeignKey(Question, on_delete = 'null')
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name