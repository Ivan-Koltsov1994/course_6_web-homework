from django import forms

from catalog.models import Product

#Cписок запрещенных слов
stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForms(forms.ModelForm):
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