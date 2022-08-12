from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import News_page, Login, Registration, Breaking_news, Logout

urlpatterns = [
	path('', News_page.as_view(), name='news_page'),
	path('logging/', Login.as_view(), name='logging'),
	path('registration/', Registration.as_view(), name='registration'),
	path('breaking_news/', Breaking_news.as_view(), name='breaking_news'),
	path('logout_user/', Logout.as_view(), name='logout_user')
] 