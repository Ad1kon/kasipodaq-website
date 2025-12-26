from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class NewsArticle(models.Model):
    """News article model for the website."""
    
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL (slug)',
        blank=True
    )
    content = RichTextField(
        verbose_name='Содержание'
    )
    image = models.ImageField(
        upload_to='news_images/',
        verbose_name='Изображение',
        blank=True,
        null=True
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-publication_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Auto-generate slug from title if not provided."""
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
