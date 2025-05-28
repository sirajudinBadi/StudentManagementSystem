from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Fees, Salary
from django.contrib import messages


# Create your views here.
@login_required
def add_fees_collection(request):
  if request.method == "POST":
    student_id = request.POST.get('student_id')
    student_name = request.POST.get('student_name')
    gender = request.POST.get('gender')
    fees_type = request.POST.get('fees_type')
    fees_amount = request.POST.get('fees_amount')
    # paid_date = request.POST.get('paid_date')
    
    fees = Fees.objects.create(
      student_id = student_id,
      student_name = student_name,
      gender = gender,
      fees_type = fees_type,
      fees_amount = fees_amount,
      # paid_date = paid_date,
      paid_status = True,
    )
    messages.success(request, "Fees Paid Successfully")
  return render(request, "monetary/add-fees-collection.html")


@login_required
def fees_collection_list(request):
  fees_list = Fees.objects.all()
  context = {"fees_list" : fees_list, }
  return render(request, 'monetary/fees-collections.html', context)


#############################################------------------SALARY SECTION--------------------

@login_required
def add_salary(request):
  if request.method == "POST":
    staff_id = request.POST.get('staff_id')
    name = request.POST.get('name')
    gender = request.POST.get('gender')
    join_date = request.POST.get('join_date')
    salary_amount = request.POST.get('salary_amount')

    salary = Salary.objects.create(
      staff_id = staff_id,
      name = name,
      gender = gender,
      join_date = join_date,
      salary_amount = salary_amount,
      status = True,
    )
    messages.success(request, "Salary Paid Successfully")
  return render(request, 'monetary/add-salary.html')

@login_required
def salary_list(request):
  salary_list = Salary.objects.all()
  context = {"salary_list" : salary_list}
  return render(request, "monetary/salary.html", context)