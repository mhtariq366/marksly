from django.shortcuts import render, redirect, get_object_or_404
from .models import Course

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

        return redirect('course_list')
    
    return render(request, 'siteadmin/add_course.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'siteadmin/course_list.html', {'courses': courses})

def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == 'POST':
        course.course_code = request.POST.get('course_code')
        course.name = request.POST.get('name')
        course.shortname = request.POST.get('shortname')
        course.credit_hours = int(request.POST.get('credit_hours'))
        course.remarks = request.POST.get('remarks')

        course.save()
        return redirect('course_list')

    return render(request, 'siteadmin/edit_course.html', {'course': course})
