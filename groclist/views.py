from django.shortcuts import render

# Create your views here.
def groclist_page(response):
    return render(response,'groclist/groclist.html')