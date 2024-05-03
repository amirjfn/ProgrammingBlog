from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment, Like
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import ListView, DetailView


def Post(request, slug):
    article_detail = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article_detail, user=request.user, parent_id=parent_id)


    is_liked = request.user.likes.filter(article__slug=slug, user_id=request.user.id)
    if is_liked.exists():
        is_liked = True
    else:
        is_liked = False
    return render(request, 'blog/article_detail.html', context={'article_detail': article_detail, 'is_like': is_liked})




def All_post(request):
    posts = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(posts, 2)
    page_list = paginator.get_page(page_number)
    return render(request, 'blog/Posts.html', context={'posts': page_list})


# rabete makos khat 27

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    posts = category.articles.all()
    return render(request, 'blog/Posts.html', context={'posts': posts})


def Users_detail(request, id):
    users = get_object_or_404(User, id=id)
    posts = users.articlo.all()
    return render(request, 'blog/Posts.html', context={'posts': posts})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    page_list = paginator.get_page(page_number)
    return render(request, 'blog/Posts.html', context={'posts': page_list})


class ArticleList(ListView):
    queryset = Article.objects.all()
    template_name = 'blog/Posts.html'


def like(request, slug, id):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug, user_id=request.user.id)
            like.delete()
            return JsonResponse({'response': 'unliked'})
        except:
            Like.objects.create(article_id=id, user_id=request.user.id)
            return JsonResponse({'response': 'liked'})


