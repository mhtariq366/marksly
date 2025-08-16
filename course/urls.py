from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_home, name='course_home'),
    path('add-course/', views.add_course, name='add_course'),
]
