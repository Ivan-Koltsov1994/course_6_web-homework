from django import forms

from catalog.models import Product, Version

# Cписок запрещенных слов
stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class FormStyleMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForms(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'description')# Выбираем поля для формы
        # exclude = ('is_active', )  # исключает поле из формы

    def clean_name(self):
        """Функция проверяет исключения загрузки запрещенных продуктов в название"""
        cleaned_data = self.cleaned_data['name']
        if cleaned_data in stop_words:
            raise forms.ValidationError('Запрещенное название')
        return cleaned_data

    def clean_description(self):
        """Функция проверяет исключения загрузки запрещенных продуктов в описание"""
        cleaned_data = self.cleaned_data['description']
        if cleaned_data in stop_words:
            raise forms.ValidationError('Запрещенное описание')
        return cleaned_data


class ProductDescriptionForm(ProductForms):
    class Meta:
        model = Product
        fields = ('description',)

class ProductCategoryForm(ProductForms):
    class Meta:
        model = Product
        fields = ('category',)

class VersionForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):
        """Проверка валидности только одной активная версия продукта"""
        cleaned_data = self.cleaned_data['is_active']

        if cleaned_data and self.instance.product.version_set.filter(is_active=True).exclude(
                id=self.instance.id).exists():
            raise forms.ValidationError('Может существовать только одна активная версия.')
        return cleaned_data
