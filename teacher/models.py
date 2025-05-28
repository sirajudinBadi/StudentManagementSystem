from django.db import models
from django.utils.text import slugify

# Create your models here.
class Education(models.Model):
  school = models.CharField(max_length=400)
  bachelor_clg = models.CharField(max_length=400)
  masters_clg = models.CharField(max_length=400)

class Skills(models.Model):
  teacher_comm_skill = models.CharField(max_length=10)
  teacher_class_mgt_skill = models.CharField(max_length=10)
  teacher_subj_skill = models.CharField(max_length=10)
  teacher_creativity_skill = models.CharField(max_length=10)

class Responsibility(models.Model):
  teacher_subj = models.CharField(max_length=50)
  teacher_class = models.CharField(max_length=10)
  teacher_section = models.CharField(max_length=10)

# class Achievements(models.Model):
#   achievments = models.TextField()

class Teacher(models.Model):
  teacher_id = models.CharField(max_length=50)
  teacher_first_name = models.CharField(max_length=100)
  teacher_last_name = models.CharField(max_length=100)
  teacher_email = models.EmailField(unique=True)
  gender = models.CharField(max_length=20, choices=[('Male', "Male"), ("Female", "Female"), ("Other", "Other")])
  teacher_dob = models.DateField()
  teacher_mobile = models.CharField(max_length=20)
  teacher_join_date = models.DateField()
  teacher_qualification = models.CharField(max_length=100)
  teacher_experience = models.CharField(max_length=10)
  teacher_address = models.TextField()

  teacher_education = models.OneToOneField(Education, on_delete=models.CASCADE, null=True, blank=True)
  teacher_skills = models.OneToOneField(Skills, on_delete=models.CASCADE, null=True, blank=True)
  teacher_responsibility = models.OneToOneField(Responsibility, on_delete=models.CASCADE, null=True, blank=True)

  # teacher_achievements = models.OneToOneField(Achievements, null=True, on_delete = models.CASCADE)

  slug = models.SlugField(max_length = 255, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.teacher_first_name}-{self.teacher_last_name}-{self.teacher_id}")
    super(Teacher, self).save(*args, **kwargs)
  
  def __str__(self):
    return f"{self.teacher_first_name} {self.teacher_last_name}"
  