from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone

from django.utils.text import slugify
from teacher.models import Teacher

# Create your models here.
class Events(models.Model):
  title = models.CharField(max_length=100)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()

  @property
  def status(self):
    now = timezone.now()

    if self.start_time < now and self.end_time > now:
      return "Active"
    elif self.start_time > now:
      return "Upcoming"
    else:
      return "Completed"
  
class Happenings(models.Model):
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Happening-{self.created_at}"
  
class TeacherLesson(models.Model):
  lec_class = models.CharField(max_length=5)
  lec_section = models.CharField(max_length=5)
  lec_date = models.DateField()
  lec_start_time = models.TimeField()
  lec_end_time = models.TimeField()

  slug = models.SlugField(max_length=255, blank=True, null=True)

  @property
  def duration(self):
    today = datetime.today().date()
    start = datetime.combine(today, self.lec_start_time)
    end = datetime.combine(today, self.lec_end_time)

    if end < start:
        end += timedelta(days=1)

    return f"{int((end - start).total_seconds() / 60)}"
  # duration = models.CharField(max_length=10)

  @property
  def status(self):
     # current time (aware datetime)
    now = timezone.localtime()

    # combine date and time, then localize to timezone
    start_naive = datetime.combine(self.lec_date, self.lec_start_time)
    end_naive = datetime.combine(self.lec_date, self.lec_end_time)

    # Make start and end aware of current timezone
    start_datetime = timezone.make_aware(start_naive, timezone.get_current_timezone())
    end_datetime = timezone.make_aware(end_naive, timezone.get_current_timezone())

    # Handle next-day ending (e.g., 10 PM to 1 AM)
    if end_datetime < start_datetime:
        end_datetime += timedelta(days=1)

    # Determine status
    if start_datetime <= now <= end_datetime:
        return "In Progress"
    elif now < start_datetime:
        return "Upcoming"
    else:
        return "Completed"
  
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"Lec-{self.lec_date}")
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f"Lecture-{self.lec_date}"