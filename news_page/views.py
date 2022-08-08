from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from datetime import timedelta
from django.utils import timezone
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.views.generic import ListView


class News_page(ListView):
    model = Article
    template_name = 'news_page.html'
    context_object_name = 'articles'


def registration(request):
    if request.method == 'POST':
        form = RegistrationUser(request.POST)
        if form.is_valid():
            MyUser.objects.create_user(
                form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                last_name=form.cleaned_data['last_name'],
                first_name=form.cleaned_data['first_name'],
            )
            return HttpResponseRedirect('/news_page/logging/')
        else:
            return HttpResponse('Пользователь с таком ником уже существует!')

    else:
        form = RegistrationUser()
        return render(request, 'registration.html', {'form': form})


def logging(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return HttpResponseRedirect('/news_page/breaking_news/')
        else:
            return HttpResponse('Пользователь с таким ником не зарегистрирован')
    else:
        form = AuthenticationForm()
        return render(request, 'logging.html', {'form': form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/news_page/')


class Breaking_news(ListView):
    model = Article
    template_name = 'breaking_news.html'
    context_object_name = 'lasts_articles'

    def get_queryset(self):
        return Article.objects.filter(publication_date__gte=(timezone.now() - timedelta(1)))
