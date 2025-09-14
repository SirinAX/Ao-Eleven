from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, "main/home.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "main/product_detail.html", {"product": product})

def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductForm()
    return render(request, "main/add_product.html", {"form": form})

# --- JSON/XML Views ---
def products_json(request):
    data = serializers.serialize("json", Product.objects.all())
    return HttpResponse(data, content_type="application/json")

def products_xml(request):
    data = serializers.serialize("xml", Product.objects.all())
    return HttpResponse(data, content_type="application/xml")

def product_json(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = serializers.serialize("json", [product])
    return HttpResponse(data, content_type="application/json")

def product_xml(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = serializers.serialize("xml", [product])
    return HttpResponse(data, content_type="application/xml")
