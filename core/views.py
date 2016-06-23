from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib import auth
from django.contrib.auth.models import User
from . forms import MyUserCreationForm

from core.models import Post


class Home(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 2


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class Fiksi(ListView):
    queryset = Post.objects.filter(category='Fiksi')
    template_name = 'fiksi.html'
    paginate_by = 2
    context_object_name = 'posts'


class Berita(ListView):
    queryset = Post.objects.filter(category='Berita')
    template_name = 'berita.html'
    paginate_by = 2
    context_object_name = 'posts'

class Olahraga(ListView):
    queryset = Post.objects.filter(category='Olahraga')
    template_name = 'olahraga.html'
    paginate_by = 2
    context_object_name = 'posts'

class Teknologi(ListView):
    queryset = Post.objects.filter(category='Teknologi')
    template_name = 'teknologi.html'
    paginate_by = 2
    context_object_name = 'posts'

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/admin")
    else:
        form = MyUserCreationForm()
    return render(request, 'register.html', {
        'form': form,
    })




