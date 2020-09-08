from django.shortcuts import render
from .models import GrocList

# Create your views here.
def groclist_page(response):
    groclist = GrocList.objects.all()
    return render(response,'groclist/groclist.html',{'groclist':groclist})