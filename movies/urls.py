from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),

    path('<int:movie_id>/add_review/', views.add_review, name='movies.add_review'),  # Adding review
    path('<int:movie_id>/place_order/', views.place_order, name='movies.place_order'),  # Placing order

    path('review/update/<int:id>/', views.update_review, name='movies.update_review'),
    path('review/delete/<int:id>/', views.delete_review, name='movies.delete_review'),
    path('order/update/<int:id>/', views.update_order, name='movies.update_order'),
    path('order/delete/<int:id>/', views.delete_order, name='movies.delete_order'),

]

