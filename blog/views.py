from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Razvan Gorea',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 16, 2023'
    },
    {
        'author': 'Filip Bumbu',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 17, 2023'
    }
]

# home view triggered when user goes to an empty path or '/' path
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# about view triggered when user goes to '/about' path
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})