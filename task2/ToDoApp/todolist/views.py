from django.http import HttpResponse
from .models import Task
from django.template import loader
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, NewTaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404

@login_required(login_url='/todolist/login/')
def index(request):
    username = request.user.get_username()
    try:
        tasks = Task.objects.all().filter(owner=request.user)
        context = {'tasks': tasks, 'username': username}
    except:
        context = {'username': username}

    return render(request, 'todolist/index.html', context)



def detail(request, question_id):
    if 'switch' in request.GET:
        task = Task.objects.get(id=question_id)
        task.completed = not task.completed
        task.save()
        return HttpResponseRedirect(request.path)
    if 'delete' in request.GET:
        task = Task.objects.get(id=question_id)
        task.delete()
        return HttpResponseRedirect('/todolist/')

    try:
        task = Task.objects.get(id=question_id)
        context = {'task': task.text, 'completed':task.completed }
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'todolist/detail.html', context)

def new_task(request):
    posted = NewTaskForm(request.POST)
    if posted.is_valid():
        task = Task(text=posted.cleaned_data['text'],owner=request.user, completed=False)
        task.save()
        return HttpResponseRedirect('/todolist/')
    else:
        return render(request, 'todolist/newtask.html', {'form': NewTaskForm()})


def login_view(request):

    posted = LoginForm(request.POST)
    if posted.is_valid() and request.method == 'POST':
        username = posted.cleaned_data['username']
        password = posted.cleaned_data['password']
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user:
            print("OK",user)
            login(request, user)
            return HttpResponseRedirect('/todolist/')
        else:
            posted.add_error(None,'Invalid username/password')

            return render(request, 'todolist/login.html', {'form': posted})

    elif request.method == 'GET':
        lf = LoginForm()
        return render(request, 'todolist/login.html', {'form': lf})
    else:
        return render(request, 'todolist/login.html', {'form': posted})


def register(request):
    posted = RegisterForm(request.POST)
    if posted.is_valid():
        username = posted.cleaned_data['username']
        password = posted.cleaned_data['password']
        User.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)
        return HttpResponseRedirect('/todolist/login')

    elif request.method == 'GET':
        lf = RegisterForm()
        return render(request, 'todolist/register.html', {'form': lf})
    else:
        return render(request, 'todolist/register.html', {'form': posted})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/todolist/')
