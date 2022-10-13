# ReadMe-Two.MD 
## Tugas 6
## Savero Arkabuana
## 2106635985

### [Link Aplikasi Heroku](https://veroarkabuana-pbptugas.herokuapp.com/)
### [Link Tugas 6](https://veroarkabuana-pbptugas.herokuapp.com/todolist/)

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Tugas 6

## Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.

- Asynchronous Programming: Data dikirimkan secara _asynchronous_ baik dalam bentuk byte atau karakter dan transmisi yang digunakan adalah _half-duplex_. Dalam transmisi ini, data dicampur dengan _bit start_ dan _bit stop_. Tidak perlu ada proses sinkronisasi dan tidak perlu menunggu proses sebelumnya untuk selesai.

- Synchronous Programming: Data ditransmisikan dalam bingkai atau blok selama transmisi sinkron dan menggunakan transmisi _full-duplex_. Ketika _request_ datang, akan ada proses sinkronisasi dan harus menunggu proses itu untuk selesai menangani _request_.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma _Event-Driven Programming_. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

### Pemrograman yang digerakkan oleh peristiwa berusaha untuk menyinkronkan terjadinya berbagai proses dengan menjaga bentuk program tetap sederhana. Komponen dasar perangkat lunak yang digerakkan oleh peristiwa adalah sebagai berikut:

- _Callback Function_, biasanya disebut sebagai _event handler_, dipanggil saat proses dipicu.

- _Looping_ proses yang mengirimkan _event handler_ yang sesuai kepada setiap proses saat dipicu.

- Contoh implementasi dalam tugas ini adalah pada _button_ ```Create a new task```, ```Change Status```, dan ```Delete Task```.
    

## Jelaskan penerapan _asynchronous programming_ pada AJAX.

- Asynchronous Javascript & XML (AJAX) bekerja dengan tanpa mengubah status situs web atau melakukan _refresh_ saat mengirim dan menerima data secara _asynchronous_ dari server akhir klien.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

### Menambahkan isi ```views.py```

- Membuat _function_ ```todolist_json``` yang akan mengambil isi data dalam format bentuk ```.json``` untuk dipakai dalam html.

```
@login_required(login_url='/todolist/login/')
def todolist_json(request):
    task = ToDoListItem.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")
```
### Menambahkan isi ```urls.py```

- Menambahkan _path_ yang mengarah kepada _function_ ```todolist_json``` pada ```urls.py```.

```
from todolist.views import todolist_json

.......

path('json/', todolist_json, name='todolist_json'),
]

```

### Mengubah ```todolist.html```

- Menambahkan _tag script_ yang diperlukan dalam tugas.

```
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
```

- Membuat _function_ di dalam _tag script_ yang diperlukan dan diseuaikan dengan _function_ pada ```views.py```. Pemanggilan _function_  disesuaikan dengan _link_ pada ```urls.py```.

```
<script>

    $(document).ready(() => {
        get_task();
    })
    function create() {
        const form = $(".create_task");
        $.ajax({
            type: "POST",
            url: "/todolist/create-task/",
            data: form.serialize(),
        }).done(function (data) {
            form.trigger("reset");
            get_task();
        });
        $("#staticBackdrop").modal("hide");
    }

    function delete_task(id) {
        $.ajax({
            type: "GET",
            url: "/todolist/hapus/" + id,
            data: {csrfmiddlewaretoken: '{{ csrf_token }}'}
        }).done((data) => {
            get_task();
        })
    }

    function change_status(id) {
        $.ajax({
            type: "GET",
            url: "/todolist/cek-selesai/" + id,
            data: {csrfmiddlewaretoken: '{{ csrf_token }}', pk: id}
        }).done((data) => {
            get_task();
        })
    }

    function get_task() {
        $.ajax({
            type: "GET",
            url: "/todolist/json/"
        }).done((data) => {
            putTaskList(data);
        });
    }

    function putTaskList(data) {
        const displayTable = $('.wrapper');
        displayTable.empty();
        data.forEach(task => {
            const taskCard = `
            <div class="card" style="width: 18rem; margin-right: auto; margin-left: auto; padding-bottom: 20; margin-top: 20px;">
            <div class="card-body">
            <h4 class="card-font">${task.fields.title}</h4>
            <h6 class="card-text">${task.fields.date}</h6>
            <p class="card-font">${task.fields.description}</p>
            ${task.fields.is_finished ? "Selesai" : "Belum Selesai"} <br>
              <input type="submit" value="Change Status" class="submit" onclick="change_status(${task.pk})" />
              <input type="submit" value="Delete Task"  class="submit" onclick="delete_task(${task.pk})" />
        </div>
      </div>`
      ;
            displayTable.append(taskCard);
        })
    };
    
</script>

```

- Menambahkan _modal_ pada file html agar bisa membuat _task_ dengan menambahkan _button_ yang akan memanggil _function_ pada _tag script_ untuk melakukan penambahan task secara _asynchronous_.

```
<h3><button type="button" class="submit" data-bs-toggle="modal" data-bs-target="#staticBackdrop">Create a new task</button></h3>

.............


<div class="wrapper">

</div>
</div>


<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">Fill out your task title and description</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="card-body">
          <form class="create_task" method="POST">
              {% csrf_token %}
              <div class="card-body" style="padding-left:0.5%;margin-top: 5px; margin-bottom: 5px;">
              <h3><input 
                type="text" 
                class="form-control" 
                id="floatingInput" 
                name="title" ></h3>
                <label for="floatingInput">Title</label>
              </div>
            
              <div class="card-body" style="padding-left:0.5%;margin-top: 5px;margin-bottom: 5px;">
              <h3><textarea 
                class="form-control" 
                id="floatingDescription" 
                name="description" rows="4" cols="50"></textarea></h3>
                <label for="floatingDescription" style="padding-left:2.5%;">Description</label>
              </div>
            </form>
      </div>
      <div class="card-body">
        <h3><button type="button" class="submit" data-bs-dismiss="modal">Close</button> 
        <button type="button" class="submit" onclick="create()">Create Task</button></h3>
      </div>
    </div>
  </div>
</div>  

<h3><button class ="submit"><a href="{% url 'todolist:logout' %}" style="color:aliceblue ;">Logout</a></button></h3>
<h3>Sesi terakhir login : {{last_login}}</h3>


</body>


```

### Deployment

- Setelah selesai mengisi file-file pada todolist, _repository_ kemudian disimpan pada akun GitHub dengan menggunakan ```git add .```, ```git commit -m "commit message"```, dan ```git push```. Setelah _repository_ telah disimpan, akan di-_deploy_ menggunakan _platform_ Heroku dengan mengikuti arahan pada _template_ yang digunakan pada tugas-tugas sebelumnya ini.


