from django.shortcuts import render, get_object_or_404
from .models import NewsArticle


def index(request):
    """Homepage view displaying latest news articles."""
    news_articles = NewsArticle.objects.all()[:12]  # Display latest 12 articles
    context = {
        'news_articles': news_articles
    }
    return render(request, 'news/index.html', context)


def news_detail(request, slug):
    """News detail view displaying full article."""
    article = get_object_or_404(NewsArticle, slug=slug)
    context = {
        'article': article
    }
    return render(request, 'news/detail.html', context)


def about(request):
    """About Us page."""
    return render(request, 'news/about.html')


def contacts(request):
    """Contacts page."""
    return render(request, 'news/contacts.html')


def activities(request):
    """Activities page."""
    return render(request, 'news/activities.html')
