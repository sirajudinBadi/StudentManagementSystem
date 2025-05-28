from django.db import models
from django.utils.text import slugify


# Create your models here.
class Sports(models.Model):
  sports_id = models.CharField(max_length=20)
  sports_name = models.CharField(max_length=50)
  coach_name = models.CharField(max_length=100)
  start_year = models.DateField()

  slug = models.SlugField(max_length=255, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.sports_id}-{self.sports_name}")
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f"{self.sports_id}-{self.sports_name}"
  
class Hostel(models.Model):
  block = models.CharField(max_length=20)
  room_no = models.CharField(max_length=10)
  room_type = models.CharField(max_length=50, choices=[("Normal", "Normal"), ("AC", "AC"), ("Suite", "Suite")])
  no_of_beds = models.CharField(max_length=5)
  cost_per_bed = models.CharField(max_length=50)
  room_status = models.CharField(max_length=20, choices=[("Full", "Full"), ("Available", "Available")])

  slug = models.SlugField(max_length=255, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.block}-{self.room_no}-{self.room_type}")
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f"{self.block}-{self.room_no}-{self.room_type}"
  
class Transport(models.Model):
  route_name = models.CharField(max_length=50)
  vehicle_num = models.CharField(max_length=20)
  driver_name = models.CharField(max_length=100)
  license_num = models.CharField(max_length=20)
  driver_mobile = models.CharField(max_length=10)
  driver_address = models.TextField()

  slug = models.SlugField(max_length=255, blank=True, null=True)

  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(f"{self.route_name}-{self.vehicle_num}")
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f"{self.route_name}-{self.vehicle_num}"
