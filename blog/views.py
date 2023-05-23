from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# home view triggered when user goes to an empty path or '/' path
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# about view triggered when user goes to '/about' path
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})