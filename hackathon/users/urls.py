from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register_user, user_profile

urlpatterns = [
    path('register/', register_user),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html')),
    path('profile/', user_profile, name='user-profile')
]