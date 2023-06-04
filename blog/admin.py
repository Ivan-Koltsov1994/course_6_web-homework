from django.contrib import admin

from blog.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug', 'content')
    list_filter = ('title',)
    search_fields = ('title',)

