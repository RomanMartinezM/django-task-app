from django.urls import path
from .views import LoginView, SignUpView, getUsers, updateUser, deleteUser

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('get/', getUsers),
    path('put/<int:pk>/', updateUser),
    path('delete/<int:pk>/', deleteUser),
]