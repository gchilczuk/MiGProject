from blog.models import Post, Category, Tag, StaticHtmlPost

def posts_all():
    return Post.objects.all()

def posts_by_category(category):
    return Post.objects.filter(category__slug__iexact=category)

def posts_by_slug(slug):
    return Post.objects.filter(slug__iexact=slug)

def posts_by_tag(tag):
    return Post.objects.filter(tags__slug__iexact=tag)

def posts_by_date(year='2000', month=''):
    filters = {'posted__year__iexact' : year}
    if month:
        filters['posted__month__iexact'] = month
        
    return Post.objects.filter(**filters)

def posts_by_author(author):
    return Post.objects.filter(author__slug__iexact=author)

def categories_all():
    return Category.objects.all()

def tags_all():
    return Tag.objects.all()

def static_posts_by_title(title):
    return StaticHtmlPost.objects.filter(title__iexact=title)