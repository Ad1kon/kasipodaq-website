from django.contrib import admin
from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    """Admin configuration for NewsArticle model."""
    
    list_display = ['title', 'publication_date', 'slug']
    list_filter = ['publication_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publication_date'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'content')
        }),
        ('Медиа', {
            'fields': ('image',)
        }),
    )
