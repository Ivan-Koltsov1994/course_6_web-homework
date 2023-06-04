from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','slug', 'content')
    list_filter = ('name',)
    search_fields = ('name',)

