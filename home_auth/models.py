from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
import datetime

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, role, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, role='admin', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role,
            password=password,
            **extra_fields
        )



class CustomUser(AbstractUser):
  ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('student', "Student"),
    ("teacher", "Teacher"),
  )

  username = None
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=20, choices=ROLE_CHOICES)

  #Password Reset Fields 
  reset_token = models.CharField(max_length=40, blank=True)
  reset_token_expires = models.DateTimeField(blank=True, null=True)

  #set email as the username
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'role', ]

  objects = CustomUserManager()

  def __str__(self):
    return self.email
  
  def generate_reset_token(self):
    self.reset_token = get_random_string(40)
    self.reset_token_expires = timezone.now() + datetime.timedelta(hours=1)
    self.save()
    return self.reset_token
  
  def send_reset_email(self, request):
    token = self.generate_reset_token()
    reset_url = request.build_absolute_uri(f"/reset-password/{self.pk}/{token}/")
    send_mail(
      "Password Reset Request",
      f"Click here to reset your password : {reset_url}",
      settings.DEFAULT_FROM_EMAIL,
      [self.email],
      fail_silently=False,
    )