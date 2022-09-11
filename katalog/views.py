from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
        "list_barang" : data_barang_catalog,
        "nama" : "Savero Arkabuana",
        "id" : "2106635985",
    }
    return render(request, "katalog.html", context)