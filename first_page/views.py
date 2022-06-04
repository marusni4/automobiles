from django.shortcuts import render
from .models import Category, Product, Shop


def main_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories': categories,
               'products': products}
    return render(request, 'main.html', context)
# Create your views here.

def category_sort_id(request, i):
    categories = Category.objects.all()
    products = Product.objects.filter(categories = i)
    context = {"products": products, "categories": categories}
    return render(request, 'categories_products.html', context)

def product_detail(request, id):
    product = Product.objects.get(id= id)
    z = product.shop_set.all()
    products_in_shop = Product.objects.filter(shop__name = 'Evroopt')
    shops_for_products = Shop.objects.filter(products__title = 'Самсунг')
    context = {'product': product, 'shops':z}
    return render(request,'product_detail.html', context)

def less_forms(request):
    if request.method == 'POST':
        print(request.POST.get('login'), request.POST.get('password'))
    return render(request, 'less_forms.html')