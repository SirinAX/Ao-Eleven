from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm

APP_NAME = "Ao Eleven"
STUDENT_NAME = "Andi Hakim Himawan"

def home(request):
    products = Product.objects.all()
    context = {
        "products": products,
        "app_name": APP_NAME,
        "student_name": STUDENT_NAME,
    }
    return render(request, "main/home.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
        "app_name": APP_NAME,
        "student_name": STUDENT_NAME,
    }
    return render(request, "main/product_detail.html", context)

def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("main:home")
    else:
        form = ProductForm()
    context = {
        "form": form,
        "app_name": APP_NAME,
        "student_name": STUDENT_NAME,
    }
    return render(request, "main/add_product.html", context)

def product_confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
        "app_name": APP_NAME,
        "student_name": STUDENT_NAME,
    }
    return render(request, "main/product_confirm_delete.html", context)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("main:home")
    # Jika request bukan POST, redirect ke detail produk
    return redirect("main:product_detail", pk=pk)

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
