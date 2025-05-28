from django.contrib import admin
from .models import Teacher, Skills, Education, Responsibility
# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
  list_display = ('teacher_id', 'teacher_first_name', 'teacher_last_name', 'gender','teacher_email', 'teacher_mobile', 'teacher_dob', 'teacher_join_date', 'teacher_qualification', 'teacher_experience', 'teacher_address')
  search_fields = ('teacher_id', 'teacher_first_name', 'teacher_last_name', 'teacher_qualification')
  list_filter = ('gender', 'teacher_experience', 'teacher_qualification')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
  list_display = ('school', 'bachelor_clg', 'masters_clg')
  search_fields = ('school', 'bachelor_clg', 'masters_clg')
  list_filter = ('school', 'bachelor_clg', 'masters_clg')

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
  list_display = ('teacher_comm_skill', 'teacher_class_mgt_skill', 'teacher_subj_skill', 'teacher_creativity_skill')
  search_fields = ('teacher_comm_skill', 'teacher_class_mgt_skill', 'teacher_subj_skill', 'teacher_creativity_skill')
  list_filter = ('teacher_comm_skill', 'teacher_class_mgt_skill', 'teacher_subj_skill', 'teacher_creativity_skill')

@admin.register(Responsibility)
class ResponsibilityAdmin(admin.ModelAdmin):
  list_display = ('teacher_subj', 'teacher_section', 'teacher_class')
  search_fields = ('teacher_subj', 'teacher_section', 'teacher_class')
  list_filter = ('teacher_subj', 'teacher_section', 'teacher_class')

# @admin.register(Achievements)
# class AchievementsAdmin(admin.ModelAdmin):
#   list_display = ('achievments', )
#   search_fields = ('achievments', )
#   list_filter = ('achievments', )