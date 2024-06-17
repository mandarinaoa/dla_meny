from django.shortcuts import render
from django.http import HttpResponse
from app.models import Product

# Create your views here.

def home(request):
    prd = Product.objects.all()
    return HttpResponse(prd.name_product)
    # return render(request, "home.html", {"products":products})


def create_product(request):
    return render(request, "create_product.html")

def create_product_form(request):
    if request.method == "POST":
        name_product = request.POST.get("name_product", 'пицца')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        stars = request.POST.get('stars')
        country = request.POST.get('country')
        product_list = Product(name_product=name_product, price=price,
                               quantity=quantity, stars=stars, country=country)
        print(product_list)
        product_list.save()
        return HttpResponse(f"товар {name_product} создан!")
    else:
        return HttpResponse("Ошибка метода ")