from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/comment_page/', views.comment_page, name='comment_page'),
    path('create_new_post_page/', views.create_new_post_page, name='create_new_post_page'),
    path('create_post/', views.create_post, name='create_post'),
    path('videos/', views.video_view, name='videos'),
    path('search/', views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
