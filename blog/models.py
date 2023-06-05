from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Post(models.Model):
    """Класс для работы с моделью Постов"""
    name = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    published = models.BooleanField(verbose_name='признак публикации', default=True)
    view_count = models.PositiveIntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """Класс мета настроек"""
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)

    def increase_views(self):
        # Метод увеличивает количество просмотров
        self.view_count += 1
        self.save()