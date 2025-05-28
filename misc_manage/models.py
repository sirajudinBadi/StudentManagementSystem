from django.db import models
from django.utils.text import slugify

CLASS_CHOICES = [("LKG", "LKG"), ("UKG", "UKG"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10")]

# Create your models here.
class Holiday(models.Model):
  holiday_id = models.CharField(max_length=20)
  holiday_name = models.CharField(max_length=50)

  HOLIDAY_CHOICES = [("Public Holiday", "Public Holiday"), ("College Holiday", "College Holiday"), ("Exam Holiday", "Exam Holiday"), ("Others", "Others")]
  holiday_type = models.CharField(max_length=30, choices=HOLIDAY_CHOICES)

  holiday_start_date = models.DateField()
  holiday_end_date = models.DateField()

  def __str__(self):
    return f"{self.holiday_name}-{self.holiday_type}"
  
class Exam(models.Model):
  exam_id = models.CharField(max_length=20)
  exam_name = models.CharField(max_length=50)

  CLASS_CHOICES = [("LKG", "LKG"), ("UKG", "UKG"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10")]
  exam_class = models.CharField(max_length=10, choices=CLASS_CHOICES)

  subject = models.CharField(max_length=50)
  exam_start_time = models.TimeField()
  exam_end_time = models.TimeField()
  exam_date = models.DateField()

  slug = models.SlugField(max_length=255, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.exam_id}-{self.exam_name}-{self.exam_date}")
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.exam_id}-{self.exam_name}-{self.exam_date}"
  
class TimeTable(models.Model):
  teacher_id = models.CharField(max_length=20)
  teacher_name = models.CharField(max_length=100)
  lec_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
  lec_section = models.CharField(max_length=20)
  subject = models.CharField(max_length=50)
  lec_date = models.DateField()
  lec_start_time = models.TimeField()
  lec_end_time = models.TimeField()

  slug = models.SlugField(max_length=255, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.teacher_id}-{self.subject}-{self.lec_date}")
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.teacher_id}-{self.subject}-{self.lec_date}"
  
class Library(models.Model):
  book_id = models.CharField(max_length=20)
  book_name = models.CharField(max_length=100)
  language = models.CharField(max_length=20, choices=[("English", "English"), ("Hindi", "Hindi"), ("Gujarati", "Gujarati")])
  book_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
  
  article_type = models.CharField(max_length=20, choices=[("Book", "Book"), ("DVD", "DVD"), ("CD", "CD"), ("Newspaper", "Newspaper"), ("Magazine", "Magazine")])

  book_status = models.CharField(max_length=20, choices=[("In Stock", "In Stock"), ("Out of Stock", "Out of Stock")])

  slug = models.SlugField(max_length=255, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.book_id}-{self.book_name}-{self.language}")
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.book_id}-{self.book_name}-{self.language}"

