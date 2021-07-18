from django.contrib.auth import views as auth_views
from django.urls import path
from .views import user_register, user_profile, user_profile_edit

urlpatterns = [
    path('register/', user_register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
    path('profile/', user_profile, name='user-profile'),
    path('profile/edit', user_profile_edit, name='user-profile-edit')
]