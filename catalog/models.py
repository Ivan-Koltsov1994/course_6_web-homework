#Импортируем бибилотеку
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Класс модели Продукта"""
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='Категория')
    unit_price = models.IntegerField(verbose_name='Цена за покупку')
    creation_date = models.DateField(verbose_name='Дата создания',auto_now=True)
    modified_date = models.DateField(verbose_name='Дата последнего изменения',auto_now_add=True)

    #поле определения активных студентов
    is_active = models.BooleanField(verbose_name='активный', default=True)

    def __str__(self):
        return f'{self.name} {self.category} {self.unit_price} {self.modified_date}'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        """Класс мета-настроек"""
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)  # сортировка, '-name' - сортировка в обратном порядке


class Category(models.Model):
    """Класс модели категории Продукта"""
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        """Класс мета-настроек"""
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)  # сортировка, '-name' - сортировка в обратном порядке
