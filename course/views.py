from django.shortcuts import render, redirect
from .models import Course

def course_home(request):
    courses = Course.objects.all()
    return render(request, 'course/course_home.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        course_code = request.POST.get('course_code')
        name = request.POST.get('name')
        shortname = request.POST.get('shortname')
        credit_hours = int(request.POST.get('credit_hours'))
        remarks = request.POST.get('remarks')

        Course.objects.create(
            course_code = course_code,
            name = name,
            shortname = shortname,
            credit_hours = credit_hours,
            remarks = remarks
        )

        return redirect('course_home')
    
    return render(request, 'course/add_course.html')

def upload_course(request):
    return render(request, 'course/upload_course.html')