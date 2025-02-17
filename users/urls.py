from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.register, name='users.signup'),
    path('login/', views.login, name='users.login'),
    path('logout/', views.logout, name='users.logout'),
    path('orders/', views.orders, name='accounts.orders'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/reset_password_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"), name='password_reset_complete'),
]