from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news, name='news'),
    path('random/', views.random_article_view, name='random')
]
