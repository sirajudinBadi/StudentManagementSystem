from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Fees, Salary

# Register your models here.
@admin.register(Fees)
class FeesAdmin(admin.ModelAdmin):
  list_display = ('student_id', 'student_name', 'gender', 'fees_type', 'fees_amount', 'paid_date', 'paid_status')
  search_fields = ('student_id', 'student_name', 'fees_type')
  list_filter = ('fees_type', 'gender', 'paid_date', 'paid_status')
  
@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
  list_display = ('staff_id', 'name', 'gender', 'salary_amount', 'join_date', 'status')
  search_fields = ('staff_id', 'name', 'salary_amount')
  list_filter = ('gender', 'join_date', 'status')
