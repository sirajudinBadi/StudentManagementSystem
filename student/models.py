from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Skills(models.Model):
  problem_solving = models.IntegerField(default=75, validators=[MinValueValidator(60), MaxValueValidator(100)], help_text="Enter Value between 60 to 100")
  technical_skill = models.IntegerField(default=75, validators=[MinValueValidator(60), MaxValueValidator(100)], help_text="Enter Value between 60 to 100")
  discipline = models.IntegerField(default=75, validators=[MinValueValidator(60), MaxValueValidator(100)], help_text="Enter Value between 60 to 100")
  communication_skill = models.IntegerField(default=75, validators=[MinValueValidator(60), MaxValueValidator(100)], help_text="Enter Value between 60 to 100")


class Parent(models.Model):
  father_name = models.CharField(max_length=100)
  father_occupation = models.CharField(max_length=100)
  father_mobile = models.CharField(max_length=20)
  father_email = models.EmailField(max_length=50)
  
  mother_name = models.CharField(max_length=100)
  mother_occupation = models.CharField(max_length=100)
  mother_mobile = models.CharField(max_length=20)
  mother_email = models.EmailField(max_length=50)
  
  present_address = models.TextField()
  permanent_address = models.TextField()

  def __str__(self):
    return f"{self.father_name} & {self.mother_name}"


class Student(models.Model):
  first_name = models.CharField(max_length = 100)
  last_name = models.CharField(max_length = 100)
  student_email = models.EmailField(max_length=50, unique=True)
  student_id = models.CharField(max_length=10)
  gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
  student_dob = models.DateField()
  student_class = models.CharField(max_length=100)
  religion = models.CharField(max_length=25)
  image = models.ImageField(upload_to='student/images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  joining_date = models.DateField()
  mobile_number = models.CharField(max_length=15)
  admission_number = models.CharField(max_length=50)
  student_section = models.CharField(max_length=50)

  skills = models.OneToOneField(Skills, on_delete=models.CASCADE)
  parent = models.OneToOneField(Parent, on_delete=models.CASCADE)
  slug = models.SlugField(max_length=255, unique=True, blank=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.first_name}-{self.last_name}-{self.student_id}")
    super(Student, self).save(*args, **kwargs)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"