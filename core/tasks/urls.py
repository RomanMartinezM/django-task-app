from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getTasks),
    path('post/', views.createTask),
    path('put/<int:pk>/', views.updateTask),
    path('delete/<int:pk>/', views.deleteTask),
]

