from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from student.models import Student
from teacher.models import Teacher
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Result(models.Model):
  student_id = models.CharField(max_length=20)
  name = models.CharField(max_length=100)
  marks = models.IntegerField(validators=[MaxValueValidator(700)])
  percentage = models.CharField(max_length=20)
  status = models.CharField(max_length=20)

  def __str__(self):
    return f"{self.student_id}-{self.name}-{self.marks}"
  
class Activity(models.Model):
  name = models.ForeignKey(Student, on_delete=models.CASCADE)
  # name = models.CharField(max_length=200)
  description = models.TextField()
  event = models.CharField(max_length=50)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.name}-{self.event}-{self.created_at}"
  

class Announcement(models.Model):
  subject = models.CharField(max_length=200)
  title = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  is_important = models.BooleanField(default=False)
  content = models.TextField()

  def __str__(self):
    return f"Announcement-{self.subject}"
  
class SpecialSession(models.Model):
  title = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  speaker = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  duration = models.CharField(max_length=20)
  location = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.title}-{self.speaker}"
  
