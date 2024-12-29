from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_institute/', views.add_institute, name='add_institute'),
]
