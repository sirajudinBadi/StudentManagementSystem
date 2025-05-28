from django.urls import path
from . import views


urlpatterns = [
    path('add-sports/', views.add_sports, name="add_sports"),
    path('view-sports/', views.view_sports, name="view_sports"),
    path('edit-sports/<str:slug>/', views.edit_sports, name="edit_sports"),
    path('delete-sports/<str:slug>/', views.delete_sports, name="delete_sports"),
    
    path('add-hostel/', views.add_hostel, name="add_hostel"),
    path('view-hostel/', views.view_hostel, name="view_hostel"),
    path('edit-hostel/<str:slug>/', views.edit_hostel, name="edit_hostel"),
    path('delete-hostel/<str:slug>/', views.delete_hostel, name="delete_hostel"),
    
    path('add-transport/', views.add_transport, name="add_transport"),
    path('view-transport/', views.view_transport, name="view_transport"),
    path('edit-transport/<str:slug>/', views.edit_transport, name="edit_transport"),
    path('delete-transport/<str:slug>/', views.delete_transport, name="delete_transport"),
]
