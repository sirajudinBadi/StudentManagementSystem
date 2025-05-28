from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # your existing url patterns
    path('add/', views.add_student, name="add_student"),
    path('student-list/', views.student_list, name="student_list"),
    path('edit-student/<str:slug>/', views.edit_student, name="edit_student"),
    path('delete-student/<str:slug>/', views.delete_student, name="delete_student"),
    path('view-student/<str:slug>/', views.view_student, name="view_student"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)