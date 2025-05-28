from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Parent, Student, Skills
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# import datetime
from datetime import datetime
# Create your views here.
@login_required
def add_student(request):
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    student_id = request.POST.get('student_id')
    gender = request.POST.get('gender')
    student_dob = request.POST.get('student_dob')
    student_class = request.POST.get('student_class')
    religion = request.POST.get('religion')
    joining_date = request.POST.get('joining_date')
    mobile_number = request.POST.get('mobile_number')
    admission_number = request.POST.get('admission_number')
    student_email = request.POST.get('student_email')
    student_section = request.POST.get('student_section')
    # image = request.FILES.get('image')

    father_name = request.POST.get('father_name')
    father_occupation = request.POST.get('father_occupation')
    father_mobile = request.POST.get('father_mobile')
    father_email = request.POST.get('father_email')
    mother_name = request.POST.get('mother_name')
    mother_occupation = request.POST.get('mother_occupation')
    mother_mobile = request.POST.get('mother_mobile')
    mother_email = request.POST.get('mother_email')

    present_address = request.POST.get('present_address')
    permanent_address = request.POST.get('permanent_address')

    communication_skill = request.POST.get('communication_skill')
    problem_solving = request.POST.get('problem_solving')
    discipline = request.POST.get('discipline')
    technical_skill = request.POST.get('technical_skill')

    skills = Skills.objects.create(
      communication_skill = communication_skill,
      problem_solving = problem_solving,
      discipline = discipline,
      technical_skill = technical_skill,
    )

    parent = Parent.objects.create(
      father_name = father_name,
      father_occupation = father_occupation,
      father_email = father_email,
      father_mobile = father_mobile,
      mother_name = mother_name,
      mother_occupation = mother_occupation,
      mother_email = mother_email,
      mother_mobile = mother_mobile,
      present_address = present_address,
      permanent_address = permanent_address,
    )

    student = Student.objects.create(
      first_name = first_name,
      last_name = last_name,
      student_email = student_email,
      gender = gender,
      student_id = student_id,
      # image = image,
      student_dob = student_dob,
      religion = religion,
      student_class = student_class,
      joining_date = joining_date,
      mobile_number = mobile_number,
      student_section = student_section,
      admission_number = admission_number,
      parent = parent,
      skills = skills,
    )

    messages.success(request, "Student Added Successfully")
  return render(request, "student/add-student.html")

@login_required
def student_list(request):
  student_list = Student.objects.select_related('parent', 'skills').all()
  context = {
    'student_list' : student_list,
  }
  return render(request, 'student/students.html', context)


@login_required
def edit_student(request, slug):
  student = get_object_or_404(Student, slug=slug)
  skills = student.skills if hasattr(student, 'skills') else None
  parent = student.parent if hasattr(student, 'parent') else None
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    student_id = request.POST.get('student_id')
    gender = request.POST.get('gender')
    student_class = request.POST.get('student_class')
    religion = request.POST.get('religion')
    mobile_number = request.POST.get('mobile_number')
    admission_number = request.POST.get('admission_number')
    student_email = request.POST.get('student_email')
    student_section = request.POST.get('student_section')
    student_dob = datetime.strptime(request.POST.get('student_dob'), "%b. %d, %Y").date()
    joining_date = datetime.strptime(request.POST.get('joining_date'), "%b. %d, %Y").date()
    # image = request.FILES.get('image')

    parent.father_name = request.POST.get('father_name')
    parent.father_occupation = request.POST.get('father_occupation')
    parent.father_mobile = request.POST.get('father_mobile')
    parent.father_email = request.POST.get('father_email')
    parent.mother_name = request.POST.get('mother_name')
    parent.mother_occupation = request.POST.get('mother_occupation')
    parent.mother_mobile = request.POST.get('mother_mobile')
    parent.mother_email = request.POST.get('mother_email')

    parent.present_address = request.POST.get('present_address')
    parent.permanent_address = request.POST.get('permanent_address')
    parent.save()

    skills.communication_skill = request.POST.get('communication_skill')
    skills.problem_solving = request.POST.get('problem_solving')
    skills.discipline = request.POST.get('discipline')
    skills.technical_skill = request.POST.get('technical_skill')
    skills.save()
    

    student.first_name = first_name
    student.last_name = last_name
    student.student_id = student_id
    student.student_email = student_email
    student.gender = gender
    student.mobile_number = mobile_number
    student.student_dob = student_dob
    student.student_class = student_class
    student.student_section = student_section
    student.religion = religion
    student.admission_number = admission_number
    student.joining_date = joining_date
    # student.image = image

    student.save()
    return redirect('student_list')
  return render(request, 'student/edit-student.html', {'student' : student, 'parent' : parent, "skills" : skills})

@login_required
def view_student(request, slug):
  student = get_object_or_404(Student, slug = slug)
  context = {
    'student' : student,
  }

  return render(request, 'student/student-details.html', context)


@login_required
def delete_student(request, slug):
  if request.method == "POST":
    student = get_object_or_404(Student, slug=slug)
    student_name = f"{student.first_name} {student.last_name}"
    student.delete()

    return redirect('student_list')
  return HttpResponseForbidden()