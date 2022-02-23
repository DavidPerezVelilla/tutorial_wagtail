from django.shortcuts import render
from django.views.generic import DetailView

from home.models import noticia

# Create your views here.
class NoticiaDetail(DetailView):
    model = noticia
    

