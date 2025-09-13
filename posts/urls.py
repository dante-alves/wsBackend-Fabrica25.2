from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('new-post/', views.post_new, name="new-post"),
    path('<int:pk>-<slug:slug>/', views.post_page, name="page"),
    path('<int:pk>-<slug:slug>/edit/', views.post_update, name="update"),
    path('<int:pk>-<slug:slug>/delete/', views.post_delete, name="delete"),
]