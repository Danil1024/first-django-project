from django.urls import path
from .views import news_page, logging, registration, breaking_news, logout_user

urlpatterns = [
	path('', news_page, name='news_page'),
	path('logging/', logging, name='logging'),
	path('registration/', registration, name='registration'),
	path('breaking_news/', breaking_news, name='breaking_news'),
	path('logout_user/', logout_user, name='logout_user')
] 