from django.urls import path
from . import views

urlpatterns = [
    path("add-event", views.add_event, name="add_event"),
    path("view-events", views.view_events, name="view_events"),

    path("add-happening", views.add_happening, name="add_happening"),
    path("view-happenings", views.view_happenings, name="view_happenings"),

    path("add-lesson", views.add_teacher_lesson, name="add_lesson"),
    path('view-lessons', views.view_lessons, name="view_lessons"),
    path('edit-lesson/<str:slug>/', views.edit_lesson, name="edit_lesson"),
    path('delete-lesson/<str:slug>/', views.delete_lesson, name="delete_lesson"),
]
