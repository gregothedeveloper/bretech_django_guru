from django.urls import path
from .views import index , homepage, task_list

urlpatterns = [
    path('', task_list, name='task'),
    path('hello/', homepage),
    path('index/', index, name='index'),  
]

