from curses.ascii import SO
from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path("", soc_view, name="core")
]
