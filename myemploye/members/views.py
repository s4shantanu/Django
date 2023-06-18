from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'members/home.html', context)
def about(request):
    return render(request, 'members/about.html', {'title': 'About'})

