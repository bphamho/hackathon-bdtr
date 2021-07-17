from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('videos/', views.video_view, name='videos'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)