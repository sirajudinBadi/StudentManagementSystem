from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Parent, Student, Skills

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_name', 'mother_name')

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("communication_skill", "problem_solving", "technical_skill", "discipline")
    search_fields = ("communication_skill", "problem_solving", "technical_skill", "discipline")
    list_filter = ("communication_skill", "problem_solving", "technical_skill", "discipline")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_email','student_id', 'gender', 'student_dob', 'student_class', 'joining_date', 'mobile_number', 'admission_number', 'student_section', )
    search_fields = ('first_name', 'last_name', 'student_id', 'student_class', 'admission_number')
    list_filter = ('gender', 'student_class', 'student_section')
    # readonly_fields = ('image',)  # Optional: makes the image 


# admin.site.register(Student, Parent)