from django.shortcuts import render
from catalog.models import Product,  Category

def home(request):

    # В контроллер отображения главной страницы добавить выборку последних 5 товаров и вывод их в консоль
    latest_products = Product.objects.order_by('-creation_date')[:5]
    for products in latest_products:
        print(products.name)

    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')
