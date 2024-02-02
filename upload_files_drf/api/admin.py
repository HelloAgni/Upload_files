from django.contrib import admin

from .models import File


@admin.register(File)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'uploaded_at', 'processed']
    list_filter = ['uploaded_at', 'processed']
    search_fields = ['uploaded_at', 'processed']
