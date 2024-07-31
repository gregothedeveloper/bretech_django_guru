from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def homepage(request):
    return HttpResponse("The best is yet to come")

def index(request):
    context ={
        'name':'bretech Solutions'
    }
    return render(request, 'br_app/index.html', context)

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'br_app/task_list.html', {'tasks': tasks})