from django.conf.urls import url
from django.contrib import admin
from .views import HomeView, SinglePostView, AboutView, CategoryView, TagView, ArchiveView, AuthorView

urlpatterns = [
    url(r'^about/$', AboutView.as_view()),
    
    url(r'^category/(?P<slug>[^\.]+)/strona/(?P<page>[1-9]+[0-9]*)/$', CategoryView.as_view(), name='cat_page'),
    url(r'^category/(?P<slug>[^\.]+)/$', CategoryView.as_view(), name='view_blog_category'),
    
    url(r'^tag/(?P<slug>[^\.]+)/strona/(?P<page>[1-9]+[0-9]*)/$', TagView.as_view(), name='tag_page'),
    url(r'^tag/(?P<slug>[^\.]+)/$', TagView.as_view(), name='view_blog_tag'),
    
    url(r'^view/(?P<slug>[^\.]+)/$', SinglePostView.as_view(), name='view_blog_post'),
    url(r'^strona/(?P<page>[1-9]+[0-9]*)/$', HomeView.as_view(), name='home_page'),
    
    url(r'^archive/(?P<year>20[0-9]{2})/(?P<month>1?[0-2]|[1-9])/strona/(?P<page>[1-9]+[0-9]*)/$', ArchiveView.as_view(), name='arch_ym_page'),
    url(r'^archive/(?P<year>20[0-9]{2})/(?P<month>1?[0-2]|[1-9])/$', ArchiveView.as_view()),
    url(r'^archive/(?P<year>20[0-9]{2})/strona/(?P<page>[1-9]+[0-9]*)/$', ArchiveView.as_view(), name='arch_y_page'),
    url(r'^archive/(?P<year>20[0-9]{2})/$', ArchiveView.as_view()),
    
    url(r'^author/(?P<user>[a-zA-Z]*)/strona/(?P<page>[1-9]+[0-9]*)/$', AuthorView.as_view(), name='view_author_page'),
    url(r'^author/(?P<user>[a-zA-Z]*)/$', AuthorView.as_view()),
    
    url(r'^$', HomeView.as_view()),
]