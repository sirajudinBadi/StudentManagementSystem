from django.contrib import admin
from .models import Result, Activity, SpecialSession
# Register your models here.
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
  list_display = ('student_id', "name", "marks", "percentage")
  search_fields = ('student_id', "name", "marks", "percentage")
  list_filter = ('student_id', "name", "marks", "percentage")

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
  list_display = ("name", "event", "created_at")
  search_fields = ("name", "event", "created_at")
  list_filter = ("name", "event", "created_at")

@admin.register(SpecialSession)
class SpecialSessionAdmin(admin.ModelAdmin):
  list_display = ("title", "speaker", "start_time", "end_time", "duration", "created_at")
  search_field = ("title", "speaker",)
  list_filter = ( "speaker", "start_time", "end_time", "duration", "created_at")
