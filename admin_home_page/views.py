import requests
from django.shortcuts import render, redirect, get_object_or_404
from student.models import Student
from teacher.models import Teacher
from monetary.models import Fees, Salary
from admin_home_page.models import Result, Activity, Announcement, SpecialSession
from misc_manage.models import Holiday
from dashboard_mgt2.models import Events, Happenings, TeacherLesson
from django.db.models import Count
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.utils import timezone
from datetime import datetime, timedelta

from django.db.models.functions import TruncMonth
from django.db.models import Count
import calendar



# Create your views here.
@login_required
def dashboard_view(request):
   student_count = Student.objects.count()
   teacher_count = Teacher.objects.count()

   expense = 0
   for salary in Salary.objects.all():
     expense += int(salary.salary_amount)

   if expense >= 10**7:
      expense = f"{expense / 10**7:.2f} Cr"
   elif expense >= 10**5:
      expense = f"{expense / 10**5:.2f} Lakhs"
   else:
      expense = f"{expense:,}"

   revenue = 0
   for fee in Fees.objects.all():
    revenue += int(fee.fees_amount)

   if revenue >= 10**7:
      revenue = f"{revenue / 10**7:.2f} Cr"
   elif revenue >= 10**5:
      revenue = f"{revenue / 10**5:.2f} Lakhs"
   else:
      revenue = f"{revenue:,}"


  # FOr CHART 1 Student Count based on Standard/Class
   data = Student.objects.values('student_class').annotate(count=Count('id')).order_by('student_class')
   classes = [item['student_class'] for item in data]
   class_count = [item['count'] for item in data]

  #Chart 2 based on Gender
   gender_data = Student.objects.values('gender').annotate(count=Count("id"))
   genders = [item['gender'] for item in gender_data]
   gender_count = [item['count'] for item in gender_data]

   star_students = Result.objects.all().order_by('-percentage')[:10]

   student_activities = Activity.objects.all().order_by('-created_at')[:5]
   students = Student.objects.all()
  # student_names = [f"{s.first_name} {s.last_name}" for s in students]

   teachers = Teacher.objects.all()
   spl_sessions = SpecialSession.objects.filter(end_time__gt=timezone.now()).order_by('end_time')[:2]

   announcements = Announcement.objects.all().order_by('-created_at')

#   #QUOTE GENERATION USING API
#    api_url = 'https://api.api-ninjas.com/v1/quotes'
#    response = requests.get(api_url, headers={'X-Api-Key': 'LHU4SCa6aTSl9a13qlkw3A==OHqRaFWLu7xWA3zG'})
#    if response.status_code == requests.codes.ok:
      
#       quote_data = response.text
#       data = json.loads(quote_data)
#       if data[0].get('category') in ["education", "business", "communication", "courage", "environmental", "success", "life", "learning", "leadership", "knowledge", "inspirational", "imagination", "graduation", "forgiveness"]:
#         random_quote = data[0].get("quote")
#         author = data[0].get("author")
#         # random_quote = response.text
#         # author = response.text
#       else:
#         random_quote = "Stay positive and keep moving forward!"
#         author = "Random Guy"

   #THIS MODEL EXISTS IN dashboard_mgt2 app
   events = Events.objects.filter(end_time__gt=timezone.now()).order_by('start_time')

   # holiday = False
   # today = datetime.now().strftime("%B %d, %Y")
   # today_day = datetime.now().strftime('%A') != "Sunday"
   # for holiday in Holiday.objects.all():
   #    if today < holiday.holiday_start_date and today > holiday.holiday_end_date and today_day:
   #       holiday = False
   #    else:
   #       holiday = True

   is_holiday = False
   today = datetime.now().date()
   today_day = datetime.now().strftime('%A')

   if today_day != "Sunday":
      for h in Holiday.objects.all():
         if h.holiday_start_date <= today <= h.holiday_end_date:
            is_holiday = True
            break


   happenings = Happenings.objects.filter(created_at__gt=timezone.now() - timedelta(days=15)).order_by('-created_at')
   

   lessons = TeacherLesson.objects.all()
   teacher_lessons = [lesson for lesson in lessons if lesson.status == "Upcoming"]
   # teacher_lessons = TeacherLesson.objects.filter(status = "Upcoming").order_by('lec_date', 'lec_start_time')
   teacher = None
   
   if request.user.role == "teacher":
      teacher = Teacher.objects.get(teacher_first_name = request.user.first_name, teacher_last_name = request.user.last_name)

   complete_count = [lesson for lesson in lessons if lesson.status == "Completed"]
   
   lesson_count = 0
   sem_progress = 0
   if lesson_count <= 80:
      lesson_count = len(complete_count)
      sem_progress = int((lesson_count/80)*100)
   else:
      lesson_count = 80
      sem_progress = 100


   # TEACHING HISTORY SECTION
   teaching_log = TeacherLesson.objects.all().order_by('-lec_date', 'lec_start_time')[:5]

   #CALENDAR SECTION
   today_lec = TeacherLesson.objects.filter(lec_date = today)
   today_lec_count = TeacherLesson.objects.filter(lec_date = today).count()


   #CHART DATA
   monthly_lessons = (
    TeacherLesson.objects
    .annotate(month=TruncMonth('lec_date'))
    .values('month')
    .annotate(lesson_count=Count('id'))
    .order_by('month')
   )

   # Format the data for ApexCharts
   months = [calendar.month_name[item['month'].month] for item in monthly_lessons]
   monthly_lec_count = [item['lesson_count'] for item in monthly_lessons]


   context = {
      "student_count" : student_count,
      "teacher_count" : teacher_count,
      "revenue" : revenue,
      "expense" : expense,
      "classes" : classes,
      "class_count" : class_count,

      "genders" : genders,
      "gender_count" : gender_count,

      "star_students" : star_students,

      "student_activities" : student_activities,
      "students" : students,

      "announcements" : announcements,

      # "random_quote" : random_quote,
      # "author" : author,

      "teachers" : teachers,
      "spl_sessions" : spl_sessions,

      "events" : events,

      "is_holiday" : is_holiday,

      "happenings" : happenings,

      'teacher_lessons' : teacher_lessons,
      'teacher' : teacher,

      "lesson_count" : lesson_count,
      "sem_progress" : sem_progress,

      "teaching_log" : teaching_log,

      "today_lec" : today_lec,
      "today_lec_count" : today_lec_count,

      'months': months,
      'monthly_lec_count': monthly_lec_count,
   }

   return render(request, "home/index.html", context)

# @login_required
# def get_profile(request, slug):
#    if request.user.role == "teacher":
#       profile = get_object_or_404(Teacher, slug=slug)
#       context = {
#          "profile" : profile,
#       }
#       # render(request, "home/base.html", context)
#       return render(request, 'teacher/teacher-details.html', context)
#    if request.user.role == "student":
#       profile = get_object_or_404(Student, slug=slug)
#       context = {
#          "profile" : profile,
#       }
#       # render(request, "home/base.html", context)
#       return render(request, 'student/student-details.html', context)



@login_required
def add_result(request):
   if request.method == "POST":
      student_id = request.POST.get('student_id')
      name = request.POST.get('name')
      marks = request.POST.get('marks')
      # percentage = request.POST.get('percentage')

      Result.objects.create(
         student_id = student_id,
         name = name,
         marks = marks,
         percentage = round(int(marks)/7, 2),
         status = "Pass",
      )
      # messages.success(request, "Result Added Successfully")
      return redirect('view_results')
   return render(request, "admin_home_page/add-result.html")

@login_required
def view_results(request):
   result_list = Result.objects.all()
   context={
      "result_list" : result_list,
   }
   return render(request, "admin_home_page/results.html", context)


#-------------------------------------------------ADD ACTIVITY-------------------------------------------------
@login_required
def add_activity(request):
  
  if request.method == "POST":
    student_id = request.POST.get('name')
    description = request.POST.get('description')
    event = request.POST.get('event')
    student_instance = Student.objects.get(id=student_id)

    Activity.objects.create(
       name = student_instance,
       description = description,
       event = event,
    )
    return redirect('dashboard')
  students = Student.objects.all()
  
  return render(request, "admin_home_page/activity/add-activity.html", {"students" : students})


#--------------------------------------------------------Announcement Section------------------------------------------------
@login_required
def add_announcement(request):
   if request.method == "POST":
      subject = request.POST.get('subject')
      content = request.POST.get('content')
      title = request.POST.get('title')
      is_important = request.POST.get('is_important') == "on"

      Announcement.objects.create(
         subject = subject,
         content = content,
         title = title,
         is_important = is_important,
      )
      return redirect('dashboard')
   return render(request, "admin_home_page/announcements/add-announcement.html")


@login_required
def add_spl_session(request):
   if request.method == "POST":
      title = request.POST.get('title')
      teacher_id = request.POST.get('speaker')
      start_time = request.POST.get('start_time')
      end_time = request.POST.get('end_time')
      duration = request.POST.get('duration')
      location = request.POST.get('location')
      teacher_instance = Teacher.objects.get(id = teacher_id)

      SpecialSession.objects.create(
         speaker = teacher_instance,
         title = title,
         start_time = start_time,
         end_time = end_time,
         location = location,
         duration = duration,
      )
      return redirect('dashboard')
   teachers = Teacher.objects.all()
   return render(request, "admin_home_page/spl_sessions/add-session.html", {"teachers" : teachers})


@login_required
def view_spl_sessions(request):
   spl_sessions = SpecialSession.objects.all().order_by('-created_at')
   context = {
      "spl_sessions" : spl_sessions,
   }
   return render(request, "admin_home_page/spl_sessions/view-sessions.html", context)


