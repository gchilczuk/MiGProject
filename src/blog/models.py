from django.db import models
from django.db.models import permalink
from tinymce.models import HTMLField
from .custom.blog_parser import blog_body_cut
from .custom.unique_slug import unique_slugify
from unidecode import unidecode
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = HTMLField()
    photo_rep = models.ImageField(upload_to='photos/%Y%m%d_%H%m', blank=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag')
    author = models.ManyToManyField('Author')
    first_p = models.TextField(default=" ")

    class Meta:
        ordering = ["-posted"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            slug = unidecode(self.title)
            unique_slugify(self, slug)
        self.first_p = blog_body_cut(self.body)
        super(Post, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            slug = unidecode(self.title)
            unique_slugify(self, slug)
        super(Category, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            slug = unidecode(self.title)
            unique_slugify(self, slug)
        super(Tag, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_tag', None, { 'slug': self.slug })

class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            slug = unidecode(self.name)
            unique_slugify(self, slug)
        super(Author, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('view_author_page', None, { 'user': self.slug, 'page': '1' })


class StaticHtmlPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

