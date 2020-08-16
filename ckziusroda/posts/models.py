from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from markdown import markdown
import os


class ImageBase(models.Model):
    file = models.FileField(upload_to='images')

    class Meta:
        abstract = True
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"

    def filename(self):
        return os.path.basename(self.file.name)

    def render(self):
        return render_to_string('posts/content/image.html', {'item': self})


class VideoBase(models.Model):
    url = models.URLField()

    class Meta:
        abstract = True
        verbose_name = "Film"
        verbose_name_plural = "Filmy"

    def render(self):
        return render_to_string('posts/content/video.html', {'item': self})

############
### NEWS ###
############


class News(models.Model):
    title = models.CharField(
        max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Aktualność"
        verbose_name_plural = "Aktualności"
        ordering = ['-created']

    def markdown_content(self):
        if self.content:
            return mark_safe(markdown(self.content))
        return ""

    def __str__(self):
        if self.title:
            return self.title
        return "Aktualność - {}".format(self.id)


class ImageNews(ImageBase):
    news = models.ForeignKey(
        News, related_name='images', on_delete=models.CASCADE, null=True, blank=True)


class VideoNews(VideoBase):
    news = models.ForeignKey(
        News, related_name='videos', on_delete=models.CASCADE, null=True, blank=True)

#############
### POSTS ###
#############


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(
        Category, related_name="posts", on_delete=models.SET_NULL, null=True)
    title = models.CharField(
        max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, related_name="posts", on_delete=models.SET_NULL, null=True)
    optional_authors = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posty"
        ordering = ['-created']

    def markdown_content(self):
        if self.content:
            return mark_safe(markdown(self.content))
        return ""

    def __str__(self):
        return self.title


class ImagePost(ImageBase):
    post = models.ForeignKey(Post, related_name="images",
                             on_delete=models.CASCADE, blank=True, null=True)


class VideoPost(VideoBase):
    post = models.ForeignKey(Post, related_name="videos",
                             on_delete=models.CASCADE, blank=True, null=True)
