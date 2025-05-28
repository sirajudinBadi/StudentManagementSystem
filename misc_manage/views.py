from django.shortcuts import render, redirect, get_object_or_404
from . models import Holiday, Library, Exam, TimeTable
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

# -------------------------------------------------HOLIDAY SECTION--------------------------------------------------------------
@login_required
def add_holiday(request):
  if request.method == "POST":
    holiday_id = request.POST.get('holiday_id')
    holiday_name = request.POST.get('holiday_name')
    holiday_type = request.POST.get('holiday_type')
    holiday_start_date = request.POST.get('holiday_start_date')
    holiday_end_date = request.POST.get('holiday_end_date')

    holiday = Holiday.objects.create(
      holiday_id = holiday_id,
      holiday_name = holiday_name,
      holiday_type = holiday_type,
      holiday_start_date = holiday_start_date,
      holiday_end_date = holiday_end_date,
    )
    messages.success(request, 'Holiday Added Successfully')
  return render(request, "misc_manage/add-holiday.html")

@login_required
def holiday_list(request):
  holiday_list = Holiday.objects.all()
  context = {
    "holiday_list" : holiday_list,
  }
  return render(request, "misc_manage/holiday.html", context)



#--------------------------------------------------------------EXAM SECTION--------------------------------------------------------
@login_required
def add_exam(request):
  if request.method == "POST":
    exam_id = request.POST.get('exam_id')
    exam_name = request.POST.get('exam_name')
    exam_class = request.POST.get('exam_class')
    subject = request.POST.get('subject')
    exam_start_time = request.POST.get('exam_start_time')
    exam_end_time = request.POST.get('exam_end_time')
    exam_date = request.POST.get('exam_date')

    exam = Exam.objects.create(
      exam_id = exam_id,
      exam_name = exam_name,
      exam_class = exam_class,
      subject = subject,
      exam_start_time = exam_start_time,
      exam_end_time = exam_end_time,
      exam_date = exam_date,
    )
    messages.success(request, "Exam Added Successfully")
  return render(request, "misc_manage/add-exam.html")

@login_required
def exam_list(request):
  exam_list = Exam.objects.all()
  context = {
    "exam_list" : exam_list,
  }
  return render(request, "misc_manage/exam.html", context)

@login_required
def edit_exam(request, slug):
  exam = get_object_or_404(Exam, slug=slug)

  if request.method == "POST":
    exam_id = request.POST.get('exam_id')
    exam_name = request.POST.get('exam_name')
    exam_class = request.POST.get('exam_class')
    subject = request.POST.get('subject')
    exam_start_time = request.POST.get('exam_start_time')
    exam_end_time = request.POST.get('exam_end_time')
    exam_date = request.POST.get('exam_date')

    exam.exam_id = exam_id
    exam.exam_name = exam_name
    exam.exam_class = exam_class
    exam.subject = subject
    exam.exam_start_time = exam_start_time
    exam.exam_end_time = exam_end_time
    exam.exam_date = exam_date
    exam.save()

    return redirect('exam_list')
  return render(request, 'misc_manage/edit-exam.html', {"exam" : exam})

@login_required
def delete_exam(request, slug):
  if request.method == "POST":
    exam = get_object_or_404(Exam, slug=slug)
    exam.delete()
    return redirect('exam_list')
  return HttpResponseForbidden()


#--------------------------------------------------------TIMETABLE Section---------------------------------------------
@login_required
def add_timetable(request):
  if request.method == "POST":
    teacher_id = request.POST.get('teacher_id')
    teacher_name = request.POST.get('teacher_name')
    lec_class = request.POST.get('lec_class')
    lec_section = request.POST.get('lec_section')
    subject = request.POST.get('subject')
    lec_date = request.POST.get('lec_date')
    lec_start_time = request.POST.get('lec_start_time')
    lec_end_time = request.POST.get('lec_end_time')

    timetable = TimeTable.objects.create(
      teacher_id = teacher_id,
      teacher_name = teacher_name,
      lec_class = lec_class,
      lec_section = lec_section,
      subject = subject,
      lec_date = lec_date,
      lec_start_time = lec_start_time,
      lec_end_time = lec_end_time
    )
    messages.success(request, "Lecture Added Successfully")
  return render(request, "misc_manage/add-time-table.html")

@login_required
def timetable_list(request):
  timetable_list = TimeTable.objects.all()
  context = {
    "timetable_list" : timetable_list,
  }
  return render(request, "misc_manage/time-table.html", context) 

@login_required
def edit_timetable(request, slug):
  timetable = get_object_or_404(TimeTable, slug=slug)
  if request.method == "POST":
    teacher_id = request.POST.get('teacher_id')
    teacher_name = request.POST.get('teacher_name')
    lec_class = request.POST.get('lec_class')
    lec_section = request.POST.get('lec_section')
    subject = request.POST.get('subject')
    lec_date = request.POST.get('lec_date')
    lec_start_time = request.POST.get('lec_start_time')
    lec_end_time = request.POST.get('lec_end_time')

    timetable.teacher_id = teacher_id
    timetable.teacher_name = teacher_name
    timetable.lec_class = lec_class
    timetable.lec_section = lec_section
    timetable.subject = subject
    timetable.lec_date = lec_date
    timetable.lec_start_time = lec_start_time
    timetable.lec_end_time = lec_end_time
    timetable.save()
    return redirect('timetable_list')
  return render(request, "misc_manage/edit-time-table.html", {"timetable" : timetable})

@login_required
def delete_timetable(request, slug):
  if request.method == "POST":
    timetable = get_object_or_404(TimeTable, slug=slug)
    timetable.delete()
    return redirect('timetable_list')
  return HttpResponseForbidden()



#-------------------------------------------------------LIBARRY Section---------------------------------------------------

@login_required
def add_book(request):
  if request.method == "POST":
    book_id = request.POST.get('book_id')
    book_name = request.POST.get('book_name')
    language = request.POST.get('language')
    book_class = request.POST.get('book_class')
    article_type = request.POST.get('article_type')
    book_status = request.POST.get('book_status')

    book = Library.objects.create(
      book_id = book_id,
      book_name = book_name,
      language = language,
      book_class = book_class,
      article_type = article_type,
      book_status = book_status,
    )
    messages.success(request, "Book Added Successfully")
  return render(request, "misc_manage/add-books.html")

@login_required
def view_books(request):
  book_list = Library.objects.all()
  context = {
    "book_list" : book_list,
  }
  return render(request, "misc_manage/library.html", context)

@login_required
def edit_book(request, slug):
  book = get_object_or_404(Library, slug = slug)
  if request.method == "POST":
    book_id = request.POST.get('book_id')
    book_name = request.POST.get('book_name')
    language = request.POST.get('language')
    book_class = request.POST.get('book_class')
    article_type = request.POST.get('article_type')
    book_status = request.POST.get('book_status')

    book.book_id = book_id
    book.book_name = book_name
    book.language = language
    book.book_class = book_class
    book.article_type = article_type
    book.book_status = book_status
    book.save()

    return redirect('view_books')
  return render(request, "misc_manage/edit-books.html", {"book" : book})

@login_required
def delete_book(request, slug):
  if request.method == "POST":
    book = get_object_or_404(Library, slug=slug)
    book.delete()
    return redirect('view_books')
  return HttpResponseForbidden()