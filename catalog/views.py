from django.shortcuts import render
from catalog.models import Product,  Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Все продукты',
        'object_list': Product.objects.all()
    }


class ProductDetailView(DetailView):
    model = Product
    def get_context_data(self,*args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category','unit_price')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category','unit_price')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

# def home(request):
#
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Главная страница',
#     }
#     # В контроллер отображения главной страницы добавить выборку последних 5 товаров и вывод их в консоль
#     # latest_products = Product.objects.order_by('-creation_date')[:5]
#     # for products in latest_products:
#     #     print(products.name)
#
#     return render(request, 'catalog/product_list.html',context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'User {name} with phone {phone} send message: {message}')
    return render(request, 'catalog/contacts.html')

# def product(request, pk=None):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'title': product_item.name,
#         'desc': product_item.description,
#         'category': product_item.category,
#         'price': product_item.unit_price,
#         'create_date': product_item.creation_date,
#         'change_date': product_item.modified_date,
#     }
#     return render(request, 'catalog/product_detail.html', context)