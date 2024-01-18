from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_site/', views.create_site, name='create_site'),
    path('update_site/<int:pk>/', views.update_site, name='update_site'),
    path('delete_site/<int:pk>/', views.delete_site, name='delete_site'),
]