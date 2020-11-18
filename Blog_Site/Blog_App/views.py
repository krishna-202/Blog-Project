from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post,Comment
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AboutView(TemplateView):
    template_name='Blog_App/about.html'

class PostListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model=Post

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/accounts/login'
    

    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True)
