from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from .models import CustomUser
from django.contrib.auth.hashers import make_password
import re

from student.models import Student
from teacher.models import Teacher

from django.http import HttpResponse

# Create your views here.
def login_view(request):
  if request.user.is_authenticated:
    return redirect(settings.LOGIN_REDIRECT_URL)
  
  if request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email = email, password = password)

    if user is not None:
      login(request, user)
      next_url = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
      return redirect(next_url)
    else:
      return render(request, "home_auth/login.html", {"error" : "Invalid Credentials"})
    
  return render(request, 'home_auth/login.html')


def logout_view(request):
  logout(request)
  return redirect(settings.LOGOUT_REDIRECT_URL)


def signup_view(request):
  if request.user.is_authenticated:
    return redirect(settings.LOGIN_REDIRECT_URL)
  
  if request.method == "POST":
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    role = request.POST.get('role')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')


    #To catch signup time errors
    errors = {}

    if CustomUser.objects.filter(email=email).exists():
      errors['email'] = "Email already exists"
    if len(password) < 8:
      errors['password'] = "Password must be at least 8 characters"
    if password != confirm_password:
      errors['confirm_password'] = "Passwords Do Not Match"

    if not errors:
      user = CustomUser.objects.create(
        email = email,
        first_name = first_name,
        last_name = last_name,
        role = role,
        password = make_password(password), # WHY make_password?
      )

      login(request, user)
      return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, "home_auth/register.html", {'errors' : errors})
  return render(request, 'home_auth/register.html')

def forgot_password_view(request):
  if request.method == "POST":
    email = request.POST.get('email')
    try:
      user = CustomUser.objects.get(email=email)
      user.send_reset_email(request)
      return render(request, "home_auth/forgot-password.html", {'success' : "Password reeset link sent to your email"})
    except CustomUser.DoesNotExist:
      return render(request, 'home_auth/forgot-password.html', {'error' : "No account with that email exists"})
  return render(request, 'home_auth/forgot-password.html')


def reset_password_view(request, user_id, token):
  try:
    user = CustomUser.objects.get(pk=user_id)
  except CustomUser.DoesNotExist:
    return redirect('login')
  
  if not (user.reset_token == token and user.reset_token_expires and user.reset_token_expires > timezone.now()):
    return redirect('login')
  
  if request.method == "POST":
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if password != confirm_password:
      return render(request, "home_auth/reset-password.html", {"error" : "Password do not match"})
    
    user.set_password(password)
    user.reset_token = ''
    user.save()
    return redirect('login')
  
  return render(request, "home_auth/reset-password.html", {
    'user_id' : user_id,
    "token" : token,
  })

# @login_required
# def dashboard_view(request):
#   student_count = Student.objects.count()
#   teacher_count = Teacher.objects.count()

#   context = {
#     "student_count" : student_count,
#     "teacher_count" : teacher_count,
#   }

#   return render(request, "home/index.html", context)