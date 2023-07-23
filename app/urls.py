from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('users/', views.users, name='users'),
    path('new_user/', views.new_user, name='new_user'),
    path('users/<int:id>/', views.user_details, name='user_details'),
]
