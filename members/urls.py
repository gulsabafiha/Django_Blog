from django.urls import path
from .views import UserRegisterView,UserEditView, PasswordsChangeView,EditProfilePageView,CreateProfilePageView,ShowProfilePageView
from django.contrib.auth import views as auth_views
from . import views
 
urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('added_profile/',UserEditView.as_view(),name='added_profile'),
    
    path('password/',PasswordsChangeView.as_view()),
    path('password_success',views.password_success,name='password_success'),
    path('create_profile',CreateProfilePageView.as_view(),name='create_profile_page'),
    path('<str:pk>/show_profile_page',ShowProfilePageView.as_view(),name='show_profile'),
    path('<int:pk>/edit_profile_page',EditProfilePageView.as_view(),name='edit_profile'),
    
 ]

