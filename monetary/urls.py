from django.urls import path
from . import views

urlpatterns = [
    path('add-fees-collection/', views.add_fees_collection, name="add_fees_collection"),
    path('fees-collection-list/', views.fees_collection_list, name="fees_collection_list"),

    path("add-salary/", views.add_salary, name="add_salary"),
    path('salary-list/', views.salary_list, name="salary_list"),
]
