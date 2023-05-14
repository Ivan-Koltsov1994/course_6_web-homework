from django.shortcuts import render
from catalog.models import Product,  Category

def home(request):

    # В контроллер отображения главной страницы добавить выборку последних 5 товаров и вывод их в консоль
    latest_products = Product.objects.order_by('-creation_date')[:5]
    for products in latest_products:
        print(products.name)

    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'User {name} with phone {phone} send message: {message}')
    return render(request, 'catalog/contacts.html')
