from django.shortcuts import render, redirect
from .models import Dish
from .forms import DishForm
# Create your views here.

def start(request):
    return render(request, 'main/start.html')


def about(request):
    return render(request, 'main/about.html')


def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'foodmenu/index.html', {'dishes': dishes} )


def create(request):
    # Saving al the data sent in the form of the html
    forms = DishForm(request.POST or None, request.FILES or None) # receiving files also 
    if forms.is_valid():
        forms.save() # Saving the data, after hitting 'submit'
        return redirect('menu') # redirecting to the list of dishes (aka menu)
    return render(request, 'foodmenu/create.html', {'forms': forms} )


def edit_dish(request, id):
    dish=Dish.objects.get(id=id) # getting the dish with the id
    forms = DishForm(request.POST or None, request.FILES or None, instance=dish) # receiving files also
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('menu')
    return render(request, 'foodmenu/edit.html', {'forms': forms} )


def delete_dish(request, id):
    dish = Dish.objects.get(id=id) # getting the dish with the id
    dish.delete() # deleting the dish
    return redirect('menu')
