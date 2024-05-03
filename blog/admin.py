from django.contrib import admin
from . import models


class FilterByTitle(admin.SimpleListFilter):
    title = ' کلید های پر تکرار'
    parameter_name = 'title'

    def lookups(self, request, model_admin):
        return (
            ('django', 'جنگو'),
            ('python', 'پایتون'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


class CommentInLine(admin.TabularInline):
    model = models.Comment


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'show_image')
    list_editable = ('slug',)
    list_filter = ('is_published', FilterByTitle)
    search_fields = ('title', 'body')
    inlines = (CommentInLine,)




admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Like)
