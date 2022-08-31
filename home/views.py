from django.shortcuts import render,HttpResponse
from home.models import Todo

# Create your views here.
def home(request):
    #return HttpResponse("This id Todo list")
    return render(request,'home.html')

def todo(request):

    if request.method =="POST":
        name =request.POST["name"]
        desc =request.POST["desc"]
        print(name,desc)
        todo=Todo(Name=name,Desc=desc)
        todo.save()
    
    return render(request,'todo.html')

def task(request):
    allTasks=Todo.objects.all()
    context={ 'tasks': allTasks}
    #return HttpResponse("This id Todo list")
    return render(request,'task.html',context)