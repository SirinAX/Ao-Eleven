from django.shortcuts import render
from .models import Product


def home(request):
    confg = {
        'app_name': 'Ao Eleven',  
        'student_name': 'Andi Hakim Himawan',
        'class_name': 'PBP D',
        'featured': Product.objects.filter(is_featured=True)[:4],
    }
    return render(request, 'main/home.html', confg)
