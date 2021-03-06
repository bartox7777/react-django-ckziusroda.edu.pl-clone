from django.urls import path, include, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('manipulate_posts', views.PostsViewset, 'posts')
router.register('categories', views.CategoriesViewset, 'categories')

urlpatterns = [
    path('news/', views.NewsList.as_view(), name='news_list'),
    path('posts/<slug:category_slug>/',
         views.PostsByCategoryList.as_view(), name='posts_by_category'),
    path('posts/search/<str:search_phrase>/',
         views.PostsByPhraseList.as_view(), name='posts_by_phrase'),
    path('posts/date/<int:year>/<int:month>/',
         views.PostsByDateList.as_view(), name='posts_by_date'),
    path('posts/<slug:category_slug>/<slug:post_slug>/',
         views.PostBySlugDetail.as_view(), name='post_by_slug'),
    path('file/', views.DocumentCreateView.as_view(), name='upload_file')
]

urlpatterns += router.urls
