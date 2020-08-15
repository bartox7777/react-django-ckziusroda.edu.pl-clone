from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from markdown import markdown
import os


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


class ItemBase(models.Model):
    class Meta:
        abstract = True

    def render(self):
        return render_to_string('posts/content/{}.html'.format(self._meta.model_name), {'item': self})


class Image(ItemBase):
    file = models.FileField(upload_to='images')
    news = models.ForeignKey(
        News, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"


class Video(ItemBase):
    url = models.URLField()
    news = models.ForeignKey(
        News, related_name='videos', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"
