from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm  # nanti buat forms.py

# Halaman Home
def home(request):
    confg = {
        'app_name': 'Ao Eleven',  
        'student_name': 'Andi Hakim Himawan',
        'class_name': 'PBP D',
    }
    return render(request, 'main/home.html', confg)

# 1. List view semua produk
def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})

# 2. Detail view produk berdasarkan ID
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'main/product_detail.html', {'product': product})

# 3. Form untuk menambahkan produk baru
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # redirect ke list view
    else:
        form = ProductForm()
    return render(request, 'main/product_add.html', {'form': form})

# 4. Export semua produk ke JSON
def products_json(request):
    data = serializers.serialize('json', Product.objects.all())
    return HttpResponse(data, content_type='application/json')

# 5. Export semua produk ke XML
def products_xml(request):
    data = serializers.serialize('xml', Product.objects.all())
    return HttpResponse(data, content_type='application/xml')

# 6. Export detail produk ke JSON
def product_json(request, pk):
    product = Product.objects.filter(id=pk)
    data = serializers.serialize('json', product)
    return HttpResponse(data, content_type='application/json')

# 7. Export detail produk ke XML
def product_xml(request, pk):
    product = Product.objects.filter(id=pk)
    data = serializers.serialize('xml', product)
    return HttpResponse(data, content_type='application/xml')
