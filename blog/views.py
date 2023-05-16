from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Razvan Gorea',
        'title': 'The Muffin Man',
        'content': 'Do you know the Muffin Man?',
        'date_posted': 'May 16, 2023'
    },
    {
        'author': 'Filip Bumbu',
        'title': 'Star Wars Meme',
        'content': 'My favorite Star Wars meme is the one with the stormtrooper falling down the stairs.',
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