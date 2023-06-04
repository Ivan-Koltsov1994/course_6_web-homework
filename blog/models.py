from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Record(models.Model):
    """Класс модели блоговой записи"""
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(max_length=15000, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='image/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    sign_of_publication = models.BooleanField(default=True, verbose_name='активный')
    count_views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-date_of_creation',)