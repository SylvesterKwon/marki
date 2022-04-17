from django.urls import path
from .views import base_views, article_views, comment_views

app_name = 'wiki'

urlpatterns = [
    # views/base_views
    path('', base_views.index, name='index'),
    path('main_page/', base_views.main_page, name='main_page'),
    path('articles/', base_views.articles, name='articles'),
    path('search/', base_views.article_search, name='article_search'),
    path('<str:article_title>/', base_views.article, name='article'),

    # views/article_views
    path('article/create/', article_views.article_create, name='article_create'),
    path('<str:article_title>/edit/', article_views.article_edit, name='article_edit'),
    path('<str:article_title>/delete/', article_views.article_delete, name='article_delete'),

    # views/comment_views
    path('<str:article_title>/comment/', comment_views.comment_create, name='comment_create'),
]
