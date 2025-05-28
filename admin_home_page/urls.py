from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('add-result/', views.add_result, name="add_result"),
    path('view-results/', views.view_results, name="view_results"),
    path('add-activity/', views.add_activity, name="add_activity"),
    path('add-announcement/', views.add_announcement, name="add_announcement"),

    path('add-spl-session/', views.add_spl_session, name="add_spl_session"),
    path('view-spl-session/', views.view_spl_sessions, name="view_spl_sessions"),
    # path('user-profile/<str:slug>/', views.get_profile, name="get_profile"),

]
