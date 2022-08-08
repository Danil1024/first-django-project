from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import News_page, logging, registration, Breaking_news, logout_user

urlpatterns = [
	path('', News_page.as_view(), name='news_page'),
	path('logging/', logging, name='logging'),
	path('registration/', registration, name='registration'),
	path('breaking_news/', login_required(Breaking_news.as_view(), login_url='/news_page/logging/'), name='breaking_news'),
	path('logout_user/', logout_user, name='logout_user')
] 