# ReadMe.MD 
## Tugas4
## Savero Arkabuana
## 2106635985

### [Link Aplikasi Tugas4](https://veroarkabuana-pbptugas.herokuapp.com/)

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

- {% csrf_token %} Memiliki fungsi untuk membuat sebuah token yang akan membuat _value_ yang besar dan _random_ untuk masing-masing _user_. Lalu _token_ tersebut akan dibandingkan _value_ nya dari token _user_ dan yang ada pada _request_ dan apabila sesuai maka akan diterima oleh _function_ sebagai parameter yang sesuai, jika tidak sesuai maka akan ditolak oleh _function_.

- Apabila tidak ada {% csrf_token %}, maka akan ada _routing_ yang bisa diakses oleh selain _user_ dan dihapus jika ada pihak yang memiliki href untuk _link_ tersebut dan tidak akan ada proses verifikasi atas siapa yang melakukan kegiatan dalam _session_ _user_ yang sedang berlangsung.


## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

- Untuk membuat <form> secara manual tentu saja bisa. <form> secara manual dibuat dengan menggunakan {% csrf_token %} untuk _user_ yang membuat form tersebut dan _method_ "POST". Pada ```createtask.html``` terdapat pembuatan form dengan <table> yang diisi oleh <tr> yang berisikan isi _input_ yang diinginkan dan disesuaikan dengan _fields_ pada ```forms.py``` atas apa saja yang ingin dibuat dalam <form>. Lalu <form> akan divalidasi pada ```views.py``` bagian _function_ ```create_task``` untuk parameter _request_-nya dan divalidasi apakah dia untuk _user_ yang sesuai, dan apabila form sudah valid maka <form> akan disimpan dan ditampilkan sesuai dengan _looping_ yang ada pada ```todolist.html```.


## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

- Proses data berisi dari pembuatan data pada pengisian <form> di ```createtask.html```. Lalu data tersebut apabila di _submit_, akan memegang _value_ "Post" dan akan divalidasi pada _function_ ```create_task``` di ```views.py```. Data pada <form> akan disimpan pada _fields_ yang sesuai di ```forms.py``` lalu divalidasi apabila data sudah sesuai dan _user_ sudah valid. Apabila sudah sesuai dan valid, maka data akan di-_routing_ sebagai _response_ untuk mengisi _todolist.html_. Lalu pada _todolist.html_, akan ada data-data baru pada _fields_ ```models.py``` yang di-_cover_ semua pada variabel "list_todolist" untuk ditampilkan pada _looping_.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.


### Membuat aplikasi baru

- Menyalakan _virtual enviroment_ pada _cmd_ direktori yang sesuai dan membuat _app baru_ dengan _command_ ```python manage.py startapp todolist``` di _cmd_ serta menambahkan ```"todolist"``` pada ```settings.py``` untuk membuat _template_ aplikasi baru.


### Membuat path baru untuk mywatchlist

- Menambahkan ```path("todolist/", include("todolist.urls")),``` pada ```urls.py``` _project_django_.


### Menambahkan models yang dibutuhkan untuk mywatchlist

- Memasukkan _models_ yang dibutuhkan mywatchlist pada variabel-variabel yang akan dipakai dalam _file_ pada todolist.

```
from django.db import models

# Create your models here.
class ToDoListItem(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    is_finished = models.BooleanField(default=False)
```


### Melakukan Migrations di CMD

- Menjalankan _command _ ```python manage.py makemigrations``` lalu ```python manage.py migrate``` pada _cmd_ untuk melakukan migrasi skema model ke dalam _database_ Django lokal.


### Menambahkan urlpatterns pada urls.py todolist

- Berbeda dengan urlpatterns pada katalog dan mywatchlist, perlu ditambahkan potongan kode dibawah ini,

```
urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='createtask'),
    path('hapus/<int:id>', hapus, name='hapus'),
    path('cek-selesai/<int:id>', cek_selesai, name='cek-selesai'),
]
```

- agar routing bisa menampilkan halaman yang sesuai.


### Membuat forms.py

- Pembuatan ```forms.py``` dilakukan untuk membuat <form> baru yang berisikan _fields_ "title" dan "description" yang akan mengisi _fields_ tersebut pada ```models.py``` untuk di-_update_ isi _models_-nya untuk ditampilkan pada _looping_ di ```todolist.html```.

```
from todolist.models import ToDoListItem

class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDoListItem
        fields = {"title", "description"} ## disesuaikan dengan apa yang diinginkan untuk diisi pada form
```


### Mengisi views.py

- Pengisian views.py untuk login,register, dan logout disamakan dengan instruksi pada lab3 dengan perbedaan pada ```show_todolist```.

``` 
user = request.user
    data_todolist = ToDoListItem.objects.filter(user = user) ## Untuk mengakses models yang isi datanya sesuai dengan user yang sedang _login_.
```

- Perbedaan views.py dimulai dari pembuatan _function baru_ yang memiliki fungsi untuk membuat <form> baru yang awalnya menerima validasi nilai _request_ dan mengisi fields yang sesuai dengan _class_ pada ```forms.py```. Lalu pengisian _user_ dan _date_ juga divalidasi untuk user yang sedang _login_ dan waktu yang pengisian <form>. Lalu <form> akan divalidasi dan disimpan lalu di-_routing_ kepada ```todolist.html``` sebagai _response_ untuk dipakai dalam _looping_. _Looping_ akan mengiterasi variabel yang menyimpan _models_ dengan data yang sudah diisi dan menampilkan isi <form> berupa "title" dan "description".

```@login_required(login_url='/todolist/login/')
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
```

- Pembuatan _function_ untuk menghapus <form> yang disesuaikan dengan "id" dari <form> tersebut dan akan menghapusnya.

```
def hapus(request, id):
    task = ToDoListItem.objects.get(id=id)
    task.delete()
    return show_todolist(request)
```

- Pembuatan _function_ untuk mengubah status dari sebuah <form> yang disesuaikan dengan "id" dari <form> tersebut. Perubahan nilai dari _field_ yang ada pada _model_ "is_finished" dan di-_return_ kepada _function_ "show_todolist" dengan nilai _field_ yang sudah dirubah untuk dipakai dalam _looping_ di ```todolist.html```.

```
def cek_selesai(request, id):
    task = ToDoListItem.objects.get(id=id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return show_todolist(request)
```

### Mengisi file html

- Untuk pengisian ```login.html``` dan ```register.html``` sama seperti lab 3.

- Untuk pembuatan ```createtask.html``` dan ```todolist.html```, disesuaikan dengan variabel _models_ yang ingin ditampilkan. Pembuatan _button_ dengan _routing_ dan pemberian _value_ untuk setiap parameter juga dibuat agar bisa diterima oleh _function_ pada ```views.py```.

- Penjelasan html ada pada komen (ditandai dengan ##) dipotongan kode dibawah ini.

```
{% extends 'base.html' %}
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js%22%3E"> </script>
{% block content %}
<h5>User : {{user}} </h5>
<!-- <b>{{nama}}</b> -->

<table class="table table-success table-striped">
    <tr>
    <th> Judul </th>
    <th> Deskripsi </th>
    <th> Tanggal </th>
    <th> Status </th>
    <th> Selesai/Belum Selesai </th>
    <th> Hapus Task </th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for i in list_todolist %} ## Iterasi models dengan value fields pada models.py
    <tr>
        <th>{{i.title}}</th>
        <th>{{i.description}}</th>
        <th>{{i.date}}</th>
        {% if i.is_finished %}
        <th>Selesai</th>
        {% else %}
        <th>Belum Selesai</th>
        {% endif %}
        <form action="{% url 'todolist:cek-selesai' id=i.id %}" method="post">
          {% csrf_token %}
          {% if i.is_finished %} ## Mengecek nilai fields dari is_finished
          <th><button type="submit">Belum Selesai</button> ## Nilai default == False
          {% else %}
          <th><button type="submit">Selesai</button> ## Nilai default boolean sudah menjadi True
          {% endif %}
        </form>
        <form action="{% url 'todolist:hapus' id=i.id %}" method="post">
          {% csrf_token %}
          <th><button type="submit">Hapus Task</button>
        </form>
    </tr>
    {% endfor %}
</table>
<h5>Sesi terakhir login : {{ last_login }}</h5>

## routing untuk function yang sesuai untuk setiap button
<button><a href="{% url 'todolist:createtask' %}">Create Task</a></button>
<button><a href="{% url 'todolist:logout' %}">Logout</a></button>

{% endblock content %}

```


- Untuk ```createtask.html```

```
{% extends 'base.html' %}

{% block meta %}
<title>Create Task</title>
{% endblock meta %}

{% block content %}  

<h1>Create Task</h1>  

    <form method="POST" >  
        {% csrf_token %}  ## Membuat token yang sesuai dengan user yang sedang login
        <table>  
            <tr>
                <td>Title: </td>
                <td>{{form.title}}</td> ## Mengisi models dengan nilai fields yang baru
            </tr>
                    
            <tr>
                <td>Description: </td>
                <td>{{form.description}}</td> ## Mengisi models dengan nilai fields yang baru
            </tr>
            <tr>  
                <td></td>
                ## Nilai parameter berupa "Post", agar bisa diterima oleh _function_ create_task pada views.py apabila di-_submit_
                <td><input type="submit" name="submit" value="Post"/></td> 
            </tr>  
        </table>  
    </form>


{% endblock content %}

```


### Deployment

- Setelah selesai mengisi file-file pada todolist, _repository_ kemudian disimpan pada akun GitHub dengan menggunakan ```git add .```, ```git commit -m "commit message"```, dan ```git push```. Setelah _repository_ telah disimpan, akan di-_deploy_ menggunakan _platform_ Heroku dengan mengikuti arahan pada _template_ yang digunakan pada tugas-tugas sebelumnya ini.



## Sumber

https://github.com/pbp-fasilkom-ui/assignment-repository
https://docs.djangoproject.com/en/4.1/topics/http/urls/#:~:text=Django%20runs%20through%20each%20URL,a%20class%2Dbased%20view).
https://www.geeksforgeeks.org/python-virtual-environment/
https://docs.djangoproject.com/en/4.1/topics/db/models/
https://docs.djangoproject.com/en/4.1/topics/http/views/
https://stackoverflow.com/questions/48282473/how-to-make-a-loop-in-html
https://www.coursera.org/lecture/service-oriented-architecture/4-1-5-html-xml-json-rK9X5
