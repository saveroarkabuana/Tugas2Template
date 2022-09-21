# ReadMe.MD 
## Tugas3
## Savero Arkabuana
## 2106635985

### [Link Aplikasi Tugas3](https://veroarkabuana.herokuapp.com/mywatchlist/)

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Penjelasan Cara Mengimplementasikan.

Melakukan _set-up_ pembuatan aplikasi dengan menggunakan Virtual Enviroment dan melakukan _clone_ dari _template_, lalu mulai mengisi arahan _template_.

### urls.py

```urls.py``` pada ```project_django```

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path("katalog/", include("katalog.urls")),
]
```
Pada bagian ```urls.py``` di ```project_django```, ditambahkan line ```path("katalog/", include("katalog.urls"))``` yang berfungsi sebagai arahan untuk mengambil data sesuai dengan _request_.

```urls.py``` pada ```katalog```

```app_name = "katalog"

urlpatterns = [
    path("", show_katalog, name = "show_katalog"),
]
```
Pada bagian ```urls.py``` di ```katalog```, ditambahkan line ```app_name = "katalog"``` yang berfungsi untuk menambahkan _namespace_ untuk aplikasi dan line ```path("", show_katalog, name = "show_katalog")``` berfungsi sebagai arahan untuk menampilkan isi data dari _function_ ```show_katalog``` pada ```views.py``` .

### models.py

```
class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()
```

Pada bagian ```models.py```, ada proses pendefinisian _database_ yang akan disimpan pada variabel-variabel untuk dipakai pada ```views.py```.

### views.py

```
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
        "list_barang" : data_barang_catalog,
        "nama" : "Savero Arkabuana",
        "id" : "2106635985",
    }
    return render(request, "katalog.html", context)
```
Pada bagian ```views.py``` di ```katalog``` berisi _function_ ```show_katalog``` yang memuat _database_ pada ```models.py``` untuk disimpan pada variabel ```list_barang``` agar variabel bisa digunakan dalam _loop_ pada html agar bisa ditampilkan.


### html

```
{% for item in list_barang %}
    <tr>
        <th>{{item.item_name}}</th>
        <th>{{item.item_price}}</th>
        <th>{{item.item_stock}}</th>
        <th>{{item.rating}}</th>
        <th>{{item.description}}</th>
        <th>{{item.item_url}}</th>
      </tr>
    {% endfor %}
```
Pada bagian html, terdapat penambahan _loop_ yang berfungsi untuk memanggil variabel yang telah di-_define_ pada ```views.py``` dan parameter data yang diambil adalah pada variabel ```list_barang``` yang telah di-_define_ untuk mencakup semua isi _object_ pada ```models.py```. Data-data yang sesuai kemudian akan ditampilkan dalam aplikasi.

### Deployment

Setelah selesai mengisi _template_, _repository_ kemudian disimpan pada akun GitHub dengan menggunakan ```git add .```, ```git commit -m "commit message"```, dan ```git push```. Setelah _repository_ telah disimpan, akan di-_deploy_ menggunakan _platform_ Heroku dengan mengikuti arahan pada _template_ yang diberikan pada Tugas2 ini.

## Pengembangan Aplikasi dengan Virtual Environment
Dalam pengembangan sebuah aplikasi dengan python, pengembangan menggunakan Virtual Environment direkomendasikan agar mengisolasi proses pengembangan aplikasi tersebut Hal ini dikarenakan Virtual Environment berfungsi untuk menjaga dependensi proyek tetap terpisah dan tidak menyebabkan konflik _web based_ apabila proses pengembangan aplikasi dilakukan pada _web based_ yang berbeda. Pengembangan apilkasi tanpa Virtual Enviroment tetap bisa dilakukan, tapi tidak dianjurkan agar menghindari proses konflik _web based_ yang berbeda dan meng-_install_ _requirements_ berbeda untuk masing-masing _web based_.

## Sumber

https://github.com/pbp-fasilkom-ui/assignment-repository
https://docs.djangoproject.com/en/4.1/topics/http/urls/#:~:text=Django%20runs%20through%20each%20URL,a%20class%2Dbased%20view).
https://www.geeksforgeeks.org/python-virtual-environment/
https://docs.djangoproject.com/en/4.1/topics/db/models/
https://docs.djangoproject.com/en/4.1/topics/http/views/
https://stackoverflow.com/questions/48282473/how-to-make-a-loop-in-html

