from django.shortcuts import render
from blog.models import Article
from django.urls import reverse



def Home(request):
    articles = Article.objects.all()[:2]
    art = Article.objects.all().order_by('-created')[:4]
    return render(request, 'home/index.html', context={'articles': articles, 'art': art})



# def sidebar(request):
#     data = {'name': 'amir'}
#
#     return render(request, 'includes/sidebar.html', context= data )
