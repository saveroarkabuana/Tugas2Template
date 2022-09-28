from urllib import response
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render
from todolist.forms import TaskForm
from todolist.models import ToDoListItem

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todolist = ToDoListItem.objects.filter(user = user)
    context = {
    'list_todolist': data_todolist,
    'nama': 'Vero',
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        form.instance.user = request.user
        form.instance.date = datetime.datetime.now()
        if form.is_valid():
            form.save()
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            return response
    else:
        form = TaskForm()
    return render(request, "createtask.html", {'form': form})

def hapus(request, id):
    task = ToDoListItem.objects.get(id=id)
    task.delete()
    return show_todolist(request)

def cek_selesai(request, id):
    task = ToDoListItem.objects.get(id=id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return show_todolist(request)



    