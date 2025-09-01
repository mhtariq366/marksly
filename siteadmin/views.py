from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Teacher
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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

def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    
    return redirect('course_list')

def siteadmin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('course_list')
        else:
            return render(request, 'siteadmin/siteadmin_login.html', {'error': 'Not allowed'})

    return render(request, 'siteadmin/siteadmin_login.html')

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'siteadmin/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        phone_number = request.POST.get('phone_number')

        error = ''

        if not username or not password or not department:
            error = "username, password, department are mandatory fields"
        elif User.objects.filter(username=username).exists():
            error = "username already exists"

        if error:
            return render(request, 'siteadmin/add_teacher.html', {'error': error})

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        Teacher.objects.create(user=user, department=department, phone_number=phone_number)

        return redirect('teacher_list')

    return render(request, 'siteadmin/add_teacher.html')

def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    user = teacher.user

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        phone_number = request.POST.get('phone_number')

        error = ''

        if not username or not password or not department:
            error = "username, password, department are mandatory fields"
        elif User.objects.filter(username=username).exists() and username != teacher.user.username:
            error = "username already exists"

        if error:
            return render(request, 'siteadmin/edit_teacher.html', {'error': error})

        user.username = username
        user.password = password
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        teacher.department = department
        teacher.phone_number = phone_number
        teacher.save()

        return redirect('teacher_list')

    return render(request, 'siteadmin/edit_teacher.html', {'teacher': teacher})

def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()

    return render('teacher_list')

