from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, Responsibility, Skills, Education
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def add_teacher(request):
  if request.method == "POST":
    teacher_id = request.POST.get('teacher_id')
    teacher_first_name = request.POST.get('teacher_first_name')
    teacher_last_name = request.POST.get('teacher_last_name')
    teacher_email = request.POST.get('teacher_email')
    teacher_mobile = request.POST.get('teacher_mobile')
    gender = request.POST.get('gender')
    teacher_experience = request.POST.get('teacher_experience')
    teacher_dob = request.POST.get('teacher_dob')
    teacher_join_date = request.POST.get('teacher_join_date')
    teacher_qualification = request.POST.get('teacher_qualification')
    teacher_address = request.POST.get('teacher_address')

    teacher_subj = request.POST.get('teacher_subj')
    teacher_class = request.POST.get('teacher_class')
    teacher_section = request.POST.get('teacher_section')

    teacher_comm_skill = request.POST.get('teacher_comm_skill')
    teacher_class_mgt_skill = request.POST.get('teacher_class_mgt_skill')
    teacher_subj_skill = request.POST.get('teacher_subj_skill')
    teacher_creativity_skill = request.POST.get('teacher_creativity_skill')

    school = request.POST.get('school')
    bachelor_clg = request.POST.get('bachelor_clg')
    masters_clg = request.POST.get('masters_clg')

    # achievments = request.POST.get('achievments')

    education = Education.objects.create(
      school = school,
      bachelor_clg = bachelor_clg,
      masters_clg = masters_clg
    )

    skills = Skills.objects.create(
      teacher_comm_skill = teacher_comm_skill,
      teacher_creativity_skill = teacher_creativity_skill,
      teacher_class_mgt_skill = teacher_class_mgt_skill,
      teacher_subj_skill = teacher_subj_skill,
    )

    responsibility = Responsibility.objects.create(
      teacher_subj = teacher_subj,
      teacher_class = teacher_class,
      teacher_section = teacher_section,
    )

    # achievement = Achievements.objects.create(
    #   achievments = achievments,
    # )

    teacher = Teacher.objects.create(
      teacher_id = teacher_id,
      teacher_first_name = teacher_first_name,
      teacher_last_name = teacher_last_name,
      gender = gender,
      teacher_email = teacher_email,
      teacher_mobile = teacher_mobile,
      teacher_experience = teacher_experience,
      teacher_address = teacher_address,
      teacher_dob = teacher_dob,
      teacher_join_date = teacher_join_date,
      teacher_qualification = teacher_qualification,
      teacher_responsibility = responsibility,
      teacher_education = education,
      teacher_skills = skills,
    )
    messages.success(request, "Teacher Added Successfully")
  return render(request, "teacher/add-teacher.html")


@login_required
def teacher_list(request):
  teacher_list = Teacher.objects.select_related('teacher_responsibility', 'teacher_education', 'teacher_skills').all()
  context = {
    'teacher_list' : teacher_list,
  }
  return render(request, 'teacher/teachers.html', context)


@login_required
def edit_teacher(request, slug):
  teacher = get_object_or_404(Teacher, slug = slug)
  teacher_responsibility = teacher.teacher_responsibility if hasattr(teacher, 'teacher_responsibility') else None
  teacher_skills = teacher.teacher_skills if hasattr(teacher, 'teacher_skills') else None
  teacher_education = teacher.teacher_education if hasattr(teacher, 'teacher_education') else None

  if request.method == "POST":
    teacher_id = request.POST.get('teacher_id')
    teacher_first_name = request.POST.get('teacher_first_name')
    teacher_last_name = request.POST.get('teacher_last_name')
    teacher_email = request.POST.get('teacher_email')
    teacher_mobile = request.POST.get('teacher_mobile')
    gender = request.POST.get('gender')
    teacher_experience = request.POST.get('teacher_experience')
    teacher_qualification = request.POST.get('teacher_qualification')
    teacher_address = request.POST.get('teacher_address')
    teacher_dob = datetime.strptime(request.POST.get('teacher_dob'), "%b %d, %Y").date()
    teacher_join_date = datetime.strptime(request.POST.get('teacher_join_date'), "%B %d, %Y").date()

    teacher_responsibility.teacher_subj = request.POST.get('teacher_subj')
    teacher_responsibility.teacher_class = request.POST.get('teacher_class')
    teacher_responsibility.teacher_section = request.POST.get('teacher_section')
    teacher_responsibility.save()

    teacher_skills.teacher_comm_skill = request.POST.get('teacher_comm_skill')
    teacher_skills.teacher_class_mgt_skill = request.POST.get('teacher_class_mgt_skill')
    teacher_skills.teacher_subj_skill = request.POST.get('teacher_subj_skill')
    teacher_skills.teacher_creativity_skill = request.POST.get('teacher_creativity_skill')
    teacher_skills.save()

    teacher_education.school = request.POST.get('school')
    teacher_education.bachelor_clg = request.POST.get('bachelor_clg')
    teacher_education.masters_clg = request.POST.get('masters_clg')
    teacher_education.save()


    teacher.teacher_id = teacher_id
    teacher.teacher_first_name = teacher_first_name
    teacher.teacher_last_name = teacher_last_name
    teacher.gender = gender
    teacher.teacher_dob = teacher_dob
    teacher.teacher_email = teacher_email
    teacher.teacher_mobile = teacher_mobile
    teacher.teacher_experience = teacher_experience
    teacher.teacher_join_date = teacher_join_date
    teacher.teacher_address = teacher_address
    teacher.teacher_qualification = teacher_qualification
    teacher.save()
    return redirect('teacher_list')
  return render(request, 'teacher/edit-teacher.html', {'teacher' : teacher, 'teacher_responsibility' : teacher_responsibility, 'teacher_skills' : teacher_skills, 'teacher_education' : teacher_education})


@login_required
def delete_teacher(request, slug):
  if request.method == "POST":
    teacher = get_object_or_404(Teacher, slug=slug)
    teacher.delete()

    return redirect('teacher_list')
  return HttpResponseForbidden()

@login_required
def view_teacher(request, slug):
  teacher = get_object_or_404(Teacher, slug=slug)
  context = {
    "teacher" : teacher,
  }
  return render(request, 'teacher/teacher-details.html', context)