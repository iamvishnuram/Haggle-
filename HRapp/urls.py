from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name="profile"),
    path('haggle/', views.game_view, name="game"),
    path('about-us/', views.about_view, name="about"),
    path('contact-us/', views.contact_view, name="contact"),
    path('reset_password/', views.forgot_pass_view, name="forgot"),
    path('accounts/login/', views.login_view, name='login_view'),
    path('accounts/logout/', views.logout_view, name='logout_view'),
    path('accounts/signup/', views.signup_view, name="signup_view"),
    
]

