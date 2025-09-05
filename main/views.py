from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    confg = {
        'app_name': 'Ao Eleven',  
        'student_name': 'Andi Hakim Himawan',
        'class_name': 'PBP D',
        'featured': Product.objects.filter(is_featured=True)[:4],
    }
    return render(request, 'main/home.html', confg)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "main/product_detail.html", {"product": product})
