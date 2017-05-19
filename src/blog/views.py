from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from .custom.blog_filters import *
from .custom.blog_parser import blog_body_cut
from .custom.pagination import paginate
# Create your views here.

class HomeView(View):
    def get(self, request, page='1', *args, **kwargs):
        context = {}
        context['view_type'] = "HomeView"
        context['categories'] = categories_all()
        context['tags'] = tags_all()
        context['current_page'] = int(page)
        context['posts'] = paginate(posts_all(), page)
        context['proper_url'] = 'home_page'

        return render(request, "home.html", context)

class CategoryView(View):
    def get(self, request, slug='', page='1', *args, **kwargs):
        context = {}
        context['view_type'] = "CategoryView"
        context['categories'] = categories_all()
        context['tags'] = tags_all()
        context['current_page'] = int(page)        
        context['posts'] = paginate(posts_by_category(slug), page)
        context['proper_url'] = 'cat_page'
        context['slug'] = slug

        return render(request, "home.html", context)

class TagView(View):
    def get(self, request, slug='', page='1', *args, **kwargs):
        context = {}
        context['view_type'] = "TagView"
        context['categories'] = categories_all()
        context['tags'] = tags_all()
        context['current_page'] = int(page)        
        context['posts'] = paginate(posts_by_tag(slug), page)
        context['proper_url'] = 'tag_page'
        context['slug'] = slug

        return render(request, "home.html", context)
        
class ArchiveView(View):
     def get(self, request, year='2000', month='', page='1', *args, **kwargs):
        context = {}
        context['view_type'] = "ArchiveView"
        context['categories'] = categories_all()
        context['tags'] = tags_all()
        context['current_page'] = int(page)
        context['posts'] = paginate(posts_by_date(year, month), page)
        context['proper_url'] = 'arch_y_page'  
        # if month == '': context['proper_url'] = 'arch_y_page'  
        # else: context['proper_url'] = 'arch_ym_page'
        context['year'] = year
        context['month'] = month

        return render(request, "home.html", context)
        
class AuthorView(View):
     def get(self, request, user, page='1', *args, **kwargs):
        context = {}
        context['view_type'] = "AuthorView"
        context['categories'] = categories_all()
        context['tags'] = tags_all()
        context['current_page'] = int(page)
        context['posts'] = paginate(posts_by_author(user), page)
        context['proper_url'] = 'view_author_page'  
        context['user'] = user

        return render(request, "home.html", context)

class SinglePostView(View):
    def get (self, request, slug=None, *args, **kwargs):
        context = {}
        context['view_type'] = "SinglePostView"
        context['categories'] = categories_all()
        context['tags'] = tags_all()
        context['current_page'] = 0
        context['post'] = get_object_or_404(Post, slug=slug)

        return render(request, "wpis.html", context)

class AboutView(View):
    def get (self, request, *args, **kwargs):
        context = {}
        context['view_type'] = "AboutView"
        context['current_page'] = 0
        context['categories'] = categories_all()
        context['tags'] = tags_all()
        context['content'] = static_posts_by_title("about")[0]

        return render(request,"about.html", context)

class FilmRates(View):
    pass

