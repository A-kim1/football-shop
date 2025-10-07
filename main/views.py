from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        # ini buat ambil semua obj Product yg kesimpen di database nya
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406429563',
        'name': 'Amar Hakim',
        'class': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

# ini function buat ngasilin form utk nambahin data Product
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

# ini function yg pake get_object_or_404(Product, pk=id) 
# buat ngambil obj Product berdasarkan primary key (id). Jika objek tidak ditemukan, akan mengembalikan halaman 404.
@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = serializers.serialize("json", product_list)
    return HttpResponse(data, content_type="application/json")

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': product.id,
            'name': str(product.name),
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'stock': product.stock,
            'product_views': product.product_views,
            'is_featured': product.is_featured,
            'is_product_hot': product.is_product_hot,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# Ajax buat add product
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    stock = request.POST.get("stock")
    is_featured = request.POST.get("is_featured") == 'on'   # checkbox handling
    user = request.user

    new_product = Product(
        name=name,
        price=price or 0,
        description=description,
        category=category,
        thumbnail=thumbnail,
        stock=stock or 0,
        is_featured=is_featured,
        user=user,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

# TAMBAHAN utk edit product
@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)

    product.name = strip_tags(request.POST.get("name", ""))
    product.price = int(request.POST.get("price", 0))  # Konversi ke int
    product.stock = int(request.POST.get("stock", 0))  # Konversi ke int
    product.category = strip_tags(request.POST.get("category", ""))
    product.thumbnail = request.POST.get("thumbnail", "")
    product.description = strip_tags(request.POST.get("description", ""))
    product.is_featured = request.POST.get("is_featured") == "on"
    
    product.save()

    return JsonResponse({
        "status": "success",
        "message": "Product updated successfully!",
    }, status=200)

# TAMBAHAN utk delete product
@csrf_exempt
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    return JsonResponse({"status": "success", "message": "Product deleted successfully!"}, status=200)

# LOGIN dan REGISTER dan LOGOUT menggunakan AJAX
@csrf_exempt
@require_POST
def ajax_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        response = JsonResponse({
            "status": "success",
            "message": f"Welcome back, {user.username}!"
        })
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        return JsonResponse({
            "status": "error",
            "message": "Invalid username or password."
        }, status=400)


@csrf_exempt
@require_POST
def ajax_register(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if not username or not password1 or not password2:
        return JsonResponse({"status": "error", "message": "All fields are required."}, status=400)

    if password1 != password2:
        return JsonResponse({"status": "error", "message": "Passwords do not match."}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"status": "error", "message": "Username already exists."}, status=400)

    user = User.objects.create_user(username=username, password=password1)
    user.save()
    return JsonResponse({"status": "success", "message": "Account created successfully!"}, status=201)

@csrf_exempt
@require_POST
def ajax_logout(request):
    if request.user.is_authenticated:
        logout(request)
        response = JsonResponse({
            "status": "success",
            "message": "You have been logged out successfully!"
        })
        response.delete_cookie('last_login')
        return response
    else:
        return JsonResponse({
            "status": "error",
            "message": "You are not logged in."
        }, status=400)