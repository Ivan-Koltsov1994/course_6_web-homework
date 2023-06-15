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
    user = models.CharField(max_length=50, verbose_name='Создатель', **NULLABLE)

    #поле определения активных студентов
    is_active = models.BooleanField(verbose_name='активный', default=True)

    def __str__(self):
        return f'{self.name} '

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


class Version(models.Model):
    """Класс модели Версии Продукта"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number_version = models.IntegerField(verbose_name='номер версии')
    title_version = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(verbose_name='признак текущей версии', default=True)

    def __str__(self):
        return f'{self.number_version} ({self.product})'

    class Meta:
        """Класс мета-настроек"""
        verbose_name = 'версия'
        verbose_name_plural = 'версии'