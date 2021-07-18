
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('/create_new_article_page', views.create_new_article_page, name='create_new_article_page'),
    path('/create_article', views.create_article, name='create_article'),
    path('', views.all_articles, name='all_articles'),
    path('/<int:pk>', views.article_detail, name='article_detail'),
]