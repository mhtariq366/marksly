from django.shortcuts import render

def course_home(request):
    return render(request, 'course/course_home.html')

