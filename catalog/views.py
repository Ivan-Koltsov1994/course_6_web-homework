from django.shortcuts import render
from catalog.models import Product,  Category

def home(request):

    context = {
        'object_list': Product.objects.all(),
        'title': 'Главная страница',
    }
    # В контроллер отображения главной страницы добавить выборку последних 5 товаров и вывод их в консоль
    # latest_products = Product.objects.order_by('-creation_date')[:5]
    # for products in latest_products:
    #     print(products.name)

    return render(request, 'catalog/home.html',context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'User {name} with phone {phone} send message: {message}')
    return render(request, 'catalog/contacts.html')

def product(request, pk=None):
    product_item = Product.objects.get(pk=pk)
    context = {
        'title': product_item.name,
        'desc': product_item.description,
        'category': product_item.category,
        'price': product_item.unit_price,
        'create_date': product_item.creation_date,
        'change_date': product_item.modified_date,
    }
    return render(request, 'catalog/product.html', context)
