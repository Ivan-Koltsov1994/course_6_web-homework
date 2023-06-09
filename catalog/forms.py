from django import forms

from catalog.models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'description')# Выбираем поля для формы
        # exclude = ('is_active', )  # исключает поле из формы

