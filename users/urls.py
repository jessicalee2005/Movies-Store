from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
]
# so if we want a user to be logged out, we can confirm with
# a message popup on the homepage (and maybe lets change login/logout
# button on homepage navbar), but the logout implementation is finished