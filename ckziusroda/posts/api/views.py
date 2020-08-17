from rest_framework import generics
from ..models import News, Post
from .serializers import NewsSerializer, PostsSerializer, PostSerializer


class NewsListView(generics.ListAPIView):
    queryset = News.objects.filter(public=True)[:6]
    serializer_class = NewsSerializer


class PostsByCategoryList(generics.ListAPIView):
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'])
    serializer_class = PostsSerializer


class PostBySlugDetail(generics.ListAPIView):
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'], slug=self.kwargs['post_slug'])
    serializer_class = PostSerializer