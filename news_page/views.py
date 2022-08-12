from datetime import timedelta
from django.utils import timezone
from .models import *
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class News_page(ListView):
    model = Article
    template_name = 'news_page/news_page.html'
    context_object_name = 'articles'


class Breaking_news(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'news_page/breaking_news.html'
    context_object_name = 'lasts_articles'
    login_url = reverse_lazy('logging')

    def get_queryset(self):
        return Article.objects.filter(publication_date__gte=(timezone.now() - timedelta(days= 1)))
