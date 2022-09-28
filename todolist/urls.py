from django.urls import path
from todolist.views import show_todolist
 #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task

app_name = 'todolist'

urlpatterns = [
    path('', login_user, name='login'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='createtask'),

]