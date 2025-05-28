from django.urls import path
from . import views

urlpatterns = [
    path('add-holiday/', views.add_holiday, name="add_holiday"),
    path('holiday-list/', views.holiday_list, name="holiday_list"),

    path('add-exam/', views.add_exam, name="add_exam"),
    path('exam-list', views.exam_list, name="exam_list"),
    path('edit-exam/<str:slug>/', views.edit_exam, name="edit_exam"),
    path('delete-exam/<str:slug>/', views.delete_exam, name="delete_exam"),

    path("add-timetable", views.add_timetable, name="add_timetable"),
    path("timetable-list/", views.timetable_list, name="timetable_list"),
    path("edit-timetable/<str:slug>/", views.edit_timetable, name="edit_timetable"),
    path("delete-timetable/<str:slug>/", views.delete_timetable, name="delete_timetable"),

    path("add-book/", views.add_book, name="add_book"),
    path("view-books/", views.view_books, name="view_books"),
    path("edit-book/<str:slug>/", views.edit_book, name="edit_book"),
    path("delete-book/<str:slug>/", views.delete_book, name="delete_book"),
]
