from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('forgot-password/', views.forgot_password_view, name="forgot_password"),
    path('reset-password/<int:user_id>/<str:token>/', views.reset_password_view, name="reset_password"),
    # path('dashboard/', views.dashboard_view, name="dashboard"),
]
