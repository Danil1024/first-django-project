from django.urls import path
from .views import Login, Registration
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('logging/', Login.as_view(), name='logging'),
	path('registration/', Registration.as_view(), name='registration'),
	path('logout_user/', LogoutView.as_view(), name='logout_user')
] 