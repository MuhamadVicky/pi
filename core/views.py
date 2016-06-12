from django.shortcuts import render
from django.views.generic import ListView, DetailView

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



