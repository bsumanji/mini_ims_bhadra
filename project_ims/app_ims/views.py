from django.shortcuts import render
from .forms import ItemCreateForm

# Create your views here.

def item_index(request):
    return render(request, 'items/index.html')

def item_create(request):
    item_create_form = ItemCreateForm
    context = {"form": }
    return render(request, 'items/create.html')

def item_edit(request):
    return render(request, 'items/edit.html')

def item_show(request):
    return render(request, 'items/show.html')

