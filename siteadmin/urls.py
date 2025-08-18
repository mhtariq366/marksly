from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('login/', views.siteadmin_login, name='siteadmin_login'),
    path('add-course/', views.add_course, name='add_course'),
    path('edit-course/<int:id>/', views.edit_course, name='edit_course'),
    path('teacher-list/', views.teacher_list, name='teacher_list'),
    path('add-teacher/', views.add_teacher, name='add_teacher'),
]

