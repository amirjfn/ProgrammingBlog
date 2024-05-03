from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from django.utils.text import slugify
# one_delete=cascade ,set_null, protect, se_default, do_nothing

class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articlo', verbose_name='نویسنده مقاله')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی')
    title = models.CharField(max_length=70, verbose_name='عنوان')
    body = models.TextField(verbose_name='بدنه')
    slug = models.SlugField(null=True,blank=True, unique=True, verbose_name='')
    image = models.ImageField(upload_to='images/articles')
    my_file = models.FileField(upload_to='file', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()


    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')
        return format_html('<h3 style="color:red">تصویر ندارد</h3>')



    def __str__(self):
        return f'{self.title} - {self.author}'

    class Meta:
        verbose_name ='مقاله'
        verbose_name_plural = 'مقالات'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:30]

    class Meta:
        verbose_name ='نظر'
        verbose_name_plural = 'نظرات'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} - {self.article.title}'

    class Meta:
        verbose_name ='لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ('-created_at',)