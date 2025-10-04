from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core import serializers
from .models import Product, Employee
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.template.loader import render_to_string


@login_required(login_url='/login')
def home(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(owner=request.user)

    context = {
        "products": products,
        "last_login": request.COOKIES.get("last_login", "Never"),
    }
    return render(request, "main/home.html", context)


@login_required(login_url='/login')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "main/product_detail.html", context)


@login_required(login_url='/login')
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect("main:home")
    else:
        form = ProductForm()
    
    context = {
        "form": form,
    }
    return render(request, "main/add_product.html", context)


def product_confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
        "next": request.GET.get("next", reverse("main:home")),
    }
    return render(request, "main/product_confirm_delete.html", context)


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("main:home")
    return redirect("main:product_detail", pk=pk)


# --- JSON/XML Views ---
def products_json(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(owner=request.user)

    data = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price) if product.price else 0,
            'owner_id': product.owner.id,
            'owner_username': product.owner.username,
            'created_at': product.created_at.isoformat() if hasattr(product, 'created_at') else None,
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)


def products_list_ajax(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(owner=request.user)

    html = ""
    for product in products:
        html += render_to_string("main/card_product.html", {"product": product, "user": request.user})

    return JsonResponse({"html": html})


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


def add_employee(request):
    pegw = Employee.objects.create(
        name="Andi Hakim Himawan",
        age=18,
        persona="aku wibu akut"
    )
    return HttpResponse(
        f"Employee berhasil ditambahkan!: {pegw.name}, umur: {pegw.age}, Persona: {pegw.persona}"
    )


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"success": True})
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # kumpulin error sebagai string
                errors = [f"{field}: {','.join(err_list)}" 
                          for field, err_list in form.errors.items()]
                return JsonResponse({"success": False, "error": " | ".join(errors)})
    context = {"form": form}
    return render(request, "main/register.html", context)
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({"success": True})
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({"success": False, "error": "Username atau password salah"})
    return render(request, "main/login.html")



@csrf_exempt
def logout_user(request):
    logout(request)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({"success": True})
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        # kalau ada data form dikirim
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        # kalau cuma buka halaman edit pertama kali
        form = ProductForm(instance=product)

    context = {
        'form': form
    }
    return render(request, "main/edit_product.html", context)

@csrf_exempt
@require_POST
def add_product_ajax(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save(commit=False)
        product.owner = request.user
        product.save()

        # render card_product.html sebagai string HTML
        product_html = render_to_string("main/card_product.html", {
            "product": product,
            "user": request.user,
        })

        return JsonResponse({
            "success": True,
            "html": product_html,
        })
    else:
        # Tambahkan ini untuk debugging
        print("FORM ERRORS:", form.errors)  # <-- ini akan tampil di terminal
        return JsonResponse({"success": False, "error": "Invalid form"}, status=400)

