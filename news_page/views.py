from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from datetime import timedelta
from django.utils import timezone
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm


class News_page(ListView):
    model = Article
    template_name = 'news_page.html'
    context_object_name = 'articles'


class Registration(CreateView):
    form_class = RegistrationUser
    template_name = 'registration.html'
    success_url = reverse_lazy('logging')


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'logging.html'
    success_url = reverse_lazy('breaking_news')


class Logout(LogoutView):
    pass


class Breaking_news(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'breaking_news.html'
    context_object_name = 'lasts_articles'
    login_url = reverse_lazy('logging')

    def get_queryset(self):
        return Article.objects.filter(publication_date__gte=(timezone.now() - timedelta(1)))
