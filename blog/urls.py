from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.Post, name='article_detail'),
    path('all_post', views.All_post, name='all_post'),
    path('category/<int:id>', views.category_detail, name='category_detail'),
    path('users/<int:id>', views.Users_detail, name='Users_detail'),
    path('search', views.search, name='search'),
    path('like/<slug:slug>/<int:id>', views.like, name='like'),
]