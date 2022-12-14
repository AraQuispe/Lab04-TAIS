from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm, ComboForm
from .models import Product, Combos


# Create your views here.


def index(request):
    return render(request, 'index.html')


def hello(request, id):
    return HttpResponse("<h1>Hello World %s</h1>" % id)


def about(request):
    return render(request, 'about.html')


def products(request):
    prod = list(Product.objects.values())
    return render(request, 'products.html', {'productos': prod})


def create_combo(request):
    return render(request, 'create_combo.html')


# Create your views here.
def save_combo(request):
    if request.method == 'POST':
        form = ComboForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/combos/')

    else:
        form = ComboForm()

    return render(request, 'create_combo.html', {'form': form})


def save_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/productos/')

    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})


def combos(request):
    combos = Combos.objects.all()

    for combo in combos:
        for product in combo.producto.all():
            print(f'Combo %, producto %', combo, product)

    return render(request, 'combos.html', {
        'combos': combos
    })
