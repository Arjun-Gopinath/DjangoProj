from django.urls import path
from . import views 

urlpatterns = [
    path('',views.groclist_page)
]
