from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.siteadmin_login, name='siteadmin_login'),
    path('add-course/', views.add_course, name='add_course'),
    path('course-list/', views.course_list, name='course_list'),
    path('edit-course/<int:id>/', views.edit_course, name='edit_course'),
]

