from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', views.Login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('edit', views.user_edit, name='edit'),
]