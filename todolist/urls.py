from django.urls import path
from todolist.views import show_todolist
 #sesuaikan dengan nama fungsi yang dibuat
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import hapus
from todolist.views import cek_selesai
from todolist.views import todolist_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='createtask'),
    path('hapus/<int:id>', hapus, name='hapus'),
    path('cek-selesai/<int:id>', cek_selesai, name='cek-selesai'),
    path('json/', todolist_json, name='todolist_json'),
]