from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from django.shortcuts import render, get_object_or_404
from news.models import NewsStory
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

def author_profile(request, id):
    customUser = get_object_or_404(CustomUser, pk=id)
    return render(request, 'users/author_profile.html', {'author': customUser})

def articles_by_author(request, id):
    author = get_object_or_404(CustomUser, pk=id)
    articles = NewsStory.objects.filter(author=author)
    return render(request, 'articles_by_author.html', {'author': author, 'articles': articles})