from django.shortcuts import render,get_object_or_404, reverse , redirect
from catalog.models import Product,  Category,Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from django.urls import reverse_lazy, reverse
from catalog.forms import ProductForms,VersionForm,ProductDescriptionForm,ProductCategoryForm

class ProductListView(LoginRequiredMixin,ListView):
    """Класс для работы с моделью Продуктов"""
    model = Product
    extra_context = {
        'title': 'Все продукты',
    }

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset =queryset.filter(is_active = True)
        return queryset

@permission_required('catalog.set_published_product')
def change_is_published(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    product_item.toggle_is_published()
    return redirect(reverse('catalog:product_detail', args=[product_item.pk]))

class ProductDetailView(DetailView):

    """Класс для получение деталей модели Продуктов"""

    model = Product


    def get_context_data(self,*args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['title'] = self.get_object()
        return context_data


class ProductCreateView(LoginRequiredMixin,CreateView):
    """Класс для создания продуктов Продуктов"""
    model = Product
    form_class = ProductForms
    # fields = ('name', 'description', 'image', 'category','unit_price')
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        """Метод добавления создателя продукта"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    """Класс для обновления  Продуктов"""
    model = Product
    form_class = ProductForms
    template_name = 'catalog/product_form_with_formset.html'
    # fields = ('name', 'description', 'image', 'category','unit_price')
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product,Version,form=VersionForm,extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object =form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class ProductDescriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductDescriptionForm
    template_name = 'catalog/product_description.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('catalog:product_detail', kwargs={'pk': pk})

    def test_func(self):
        return self.request.user.has_perm(perm='catalog.change_description_product')

class ProductCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCategoryForm
    template_name = 'catalog/product_category.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('catalog:product_detail', kwargs={'pk': pk})

    def test_func(self):
        return self.request.user.has_perm(perm='catalog.change_product_category')


class ProductDeleteView(DeleteView):
    """Класс для удаления Продуктов"""
    model = Product
    success_url = reverse_lazy('catalog:product_list')

def toggle_activity(request, pk):
    product_item = get_object_or_404(Product,pk=pk)
    if product_item.is_active:
        product_item.is_active = False
    else:
        product_item.is_active = True

    product_item.save()

    return redirect(reverse('catalog:product_detail',args=[product_item.pk]))


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

class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request, *args, **kwargs):
        """Получение данных из формы"""
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if not name or not email or not message:
            context = {"error": "Введите все поля!"}
            return render(request, self.template_name, context=context)

        print(f'Сообщение от {name}({email}): {message}')

        context = {"success": "Сообщение успешно отправлено!"}
        return render(request, self.template_name, context=context)

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