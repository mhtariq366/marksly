from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def add_institute(request):
    return render(request, 'core/add_institute.html')


