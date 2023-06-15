from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Shantanu Raut',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 15, 2023'
    },
    {
        'author': 'Shantanu Raut',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 16, 2023'
    }
]
def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'members/home.html', context)
def about(request):
    return render(request, 'members/about.html', {'title': 'About'})

