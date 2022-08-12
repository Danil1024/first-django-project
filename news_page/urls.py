from django.urls import path
from .views import News_page, Breaking_news


urlpatterns = [
	path('', News_page.as_view(), name='news_page'),
	path('breaking_news/', Breaking_news.as_view(), name='breaking_news'),
] 