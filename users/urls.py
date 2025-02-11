from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='users.signup'),
    path('login/', views.login, name='users.login'),
    path('logout/', views.logout, name='users.logout'),
]