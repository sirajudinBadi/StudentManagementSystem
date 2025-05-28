from django.contrib import admin
from .models import Holiday, Exam, TimeTable, Library

# Register your models here.
@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
  list_display = ('holiday_id', "holiday_name", "holiday_type", "holiday_start_date", "holiday_end_date")
  search_fields = ('holiday_id', "holiday_name", "holiday_type",)
  list_filter = ("holiday_name","holiday_type")

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
  list_display = ("exam_id", "exam_name", "exam_class", "subject", "exam_start_time", "exam_end_time", "exam_date")
  search_fields = ("exam_id", "exam_name", "exam_class", "subject",)
  list_filter = ("exam_name", "exam_class", "subject", "exam_date")

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
  list_display = ("teacher_id", "teacher_name", "lec_class", "lec_section", "subject", "lec_date", "lec_start_time", "lec_end_time")
  search_fields = ("teacher_id", "teacher_name","lec_class", "subject")
  list_filter = ("teacher_name", "lec_class", "subject", "lec_date")

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
  list_display = ("book_id", "book_name", "language", "book_class", "article_type", "book_status")
  search_fields = ("book_name", "language", "book_class", "article_type", "book_status")
  list_filter = ("book_name", "language", "book_class", "article_type", "book_status")