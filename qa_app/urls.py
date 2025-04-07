from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='qa_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='qa_app/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('like/<int:pk>/', views.like_answer, name='like_answer'),
]