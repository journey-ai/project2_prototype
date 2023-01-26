from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('createform/', views.createform, name='createform'),
    path('result/', views.result),
]
