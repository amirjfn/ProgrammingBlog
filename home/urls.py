from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home, name='home'),
    # path('sidbar', views.sidebar, name='sidebar'),
]
