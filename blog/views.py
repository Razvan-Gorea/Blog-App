from django.forms import BaseModelForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse

# Django's built-in class based views

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )

from .models import Post

# home view triggered when user goes to an empty path or '/' path
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) # render the home.html template with the context dictionary containing the posts objects

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

# class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # Newest to Oldest (Display posts from newest to oldest)
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # check if the author of the post is the current user
        return super().form_valid(form)
    
    # function to check if the author of the post is the current user
    def test_func(self):
        post = self.get_object() # get the post object
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # When a post is deleted, redirect to the home page
 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False