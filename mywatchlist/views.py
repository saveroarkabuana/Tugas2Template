from django.http import HttpResponse
from django.core import serializers

# Create your views here.
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchlist(request):
    data_film_wishlist = MyWatchList.objects.all()
    context = {
    "list_film": data_film_wishlist,
    "nama" : "Vero",
    "npm" : "2106635985",
    "watched": 0,
    "selamat": ""
    }
    for i in context.get("list_film"):
        if i.watched == "yes":
            context["watched"] += 1
    if (len(context.get("list_film")) / 2) <= context["watched"]:
        context["selamat"] += "Selamat, kamu sudah banyak menonton!"
    else:
        context["selamat"] += "Wah, kamu masih sedikit menonton!"

    return render(request, "mywatchlist.html", context)
    

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
