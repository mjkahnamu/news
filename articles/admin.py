from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import Article,comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = comment
    # extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article,ArticleAdmin)
admin.site.register(comment)