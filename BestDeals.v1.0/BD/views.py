from django.shortcuts import render
from .models import Product


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def get_keywords():
    file_path = '/home/ASHOffers/BestDeals.v1.0/static/keywords.txt'  # Update with the correct path to your keywords.txt file
    with open(file_path, 'r') as file:
        keywords = file.read().splitlines()
    return keywords

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def search(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(keywords__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
