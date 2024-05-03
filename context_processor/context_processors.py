from blog.models import Article, Category
from django.contrib.auth.models import User


def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')[:3]


    return {'recent_articles': recent_articles}


def category(request):
    category = Category.objects.all()
    users = User.objects.all()
    return {'category': category, 'users': users}