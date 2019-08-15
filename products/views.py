from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your index function
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# Create your index function
def new(request):
    return HttpResponse("New product")