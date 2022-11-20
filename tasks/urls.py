from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update/<str:primary_key>/', views.update, name="update"),
    path('delete/<str:primary_key>/', views.deleteTask, name="delete"),
]
