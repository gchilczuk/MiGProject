from django.contrib import admin
from .models import Post, Category, Tag, Author, StaticHtmlPost

class PostAdmin(admin.ModelAdmin):
    exclude = ['posted', 'first_p', 'modified', 'slug']

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']

class TagAdmin(admin.ModelAdmin):
    exclude = ['slug']

class AuthorAdmin(admin.ModelAdmin):
    exclude = ['slug']

class StaticHtmlPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(StaticHtmlPost, StaticHtmlPostAdmin)