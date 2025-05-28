from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Events, Happenings, TeacherLesson
from teacher.models import Teacher
from django.contrib import messages
from django.http import HttpResponseForbidden


# Create your views here.
@login_required
def add_event(request):
  if request.method == "POST":
    title = request.POST.get('title')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')

    Events.objects.create(
      title = title,
      start_time = start_time,
      end_time = end_time,
    )
    # messages.success()
    return redirect('view_events')
  return render(request, "dashboard_mgt2/events/add-event.html")

@login_required
def view_events(request):
  event_list = Events.objects.all()
  context = {
    "event_list" : event_list,
  }
  return render(request, "dashboard_mgt2/events/view-events.html", context)


@login_required
def add_happening(request):
  if request.method == "POST":
    message = request.POST.get('message')

    Happenings.objects.create(
      message = message,
    )
    return redirect("view_happenings")
  return render(request, "dashboard_mgt2/happenings/add-happening.html")

@login_required
def view_happenings(request):
  happenings = Happenings.objects.all()
  context = {
    "happenings" : happenings,
  }
  return render(request, "dashboard_mgt2/happenings/happenings.html", context)


#----------------------------------------------     TEACHER LESSON SECTION    -----------------------------------------------
@login_required
def add_teacher_lesson(request):
  teacher = Teacher.objects.get(teacher_first_name = request.user.first_name, teacher_last_name = request.user.last_name)
  if request.method == "POST":
    # teacher_name = f"{request.user.first_name} {request.user.last_name}"

    # for teacher in Teacher.objects.all():
    # obj_teacher_name = f"{teacher.teacher_first_name} {teacher.teacher_last_name}"
    # if teacher == obj_teacher_name:
    # teacher_id = teacher.teacher_id
    # lecturer_name = f"{teacher.teacher_first_name} {teacher.teacher_last_name}"
    # subject = teacher.teacher_responsibility.teacher_subj
    lec_class = request.POST.get('lec_class')
    lec_section = request.POST.get('lec_section')
    lec_date = request.POST.get('lec_date')
    lec_start_time = request.POST.get('lec_start_time')
    lec_end_time = request.POST.get('lec_end_time')
    duration = request.POST.get('duration')
    # status = request.POST.get('status')

    TeacherLesson.objects.create(
      # teacher_id = teacher_id,
      # lecturer_name = lecturer_name,
      # subject = subject,
      lec_class = lec_class,
      lec_section = lec_section,
      lec_date = lec_date,
      lec_start_time = lec_start_time,
      lec_end_time = lec_end_time,
      # duration = duration,
      # status = status,
    )
    return redirect("view_lessons")
  return render(request, "dashboard_mgt2/lectures/add-lesson.html", {"teacher" : teacher,})


@login_required
def view_lessons(request):
  lesson_list = TeacherLesson.objects.all()
  context = {
    "lesson_list" : lesson_list,
  }
  return render(request, "dashboard_mgt2/lectures/view-lessons.html", context)

    
@login_required
def edit_lesson(request, slug):
  lesson = get_object_or_404(TeacherLesson, slug=slug)
  if request.method == "POST":
    # teacher_id = request.POST.get('teacher_id')
    # lecturer_name = request.POST.get('lecturer_name')
    # subject = request.POST.get('subject')
    lec_class = request.POST.get('lec_class')
    lec_section = request.POST.get('lec_section')
    lec_date = request.POST.get('lec_date')
    lec_start_time = request.POST.get('lec_start_time')
    lec_end_time = request.POST.get('lec_end_time')
    # duration = request.POST.get('duration')
    # status = request.POST.get('status')

    # lesson.teacher_id = teacher_id
    # lesson.lecturer_name = lecturer_name
    # lesson.subject = subject
    lesson.lec_class = lec_class
    lesson.lec_section = lec_section
    lesson.lec_date = lec_date
    lesson.lec_start_time = lec_start_time
    lesson.lec_end_time = lec_end_time
    # lesson.duration = duration
    # lesson.status = status
    lesson.save()

    return redirect('view_lessons')
  return render(request, 'dashboard_mgt2/lectures/edit-lesson.html', {"lesson" : lesson})


@login_required
def delete_lesson(request, slug):
  if request.method == "POST":
    lesson = get_object_or_404(TeacherLesson, slug=slug)
    lesson.delete()
    return redirect('view_lessons')
  return HttpResponseForbidden()




