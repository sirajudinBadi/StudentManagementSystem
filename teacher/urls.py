from django.urls import path
from . import views


urlpatterns = [
    path('add-teacher/', views.add_teacher, name="add_teacher"),
    path('teacher-list/', views.teacher_list, name="teacher_list"),
    path('edit-teacher/<str:slug>/', views.edit_teacher, name="edit_teacher"),
    path('delete-teacher/<str:slug>/', views.delete_teacher, name="delete_teacher"),
    path('view-teacher/<str:slug>/', views.view_teacher, name="view_teacher")
]
