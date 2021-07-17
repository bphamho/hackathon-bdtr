from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail')
]