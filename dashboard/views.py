from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from web . models import Book

# Create your views here.
def purple(request):

    context = {
        'hello': "enthan bro modayaano",

    }
    return render(request, 'web/purple.html', context)

class PurpleListView(ListView):
    model = Book
    template_name='web/cbv.html'



# class ModelListView(ListView):
#     model = Model
#     template_name = ".html"

