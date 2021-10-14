"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# from blog.views import post_list, post_detail
from blog.views import IndexView, CategoryView, TagView, \
    PostDetailView, SearchView, AuthorView, demo, demo_list
# from blog.apis import post_list, PostList
from blog.apis import PostViewSet, CategoryViewSet
from config.views import LinkListView
# import sys
# sys.path.append("C:\workspace\Django\\typeidea\\typeidea")
from comment.views import CommentView
from .custom_site import custom_site

router = DefaultRouter()
# router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'post', PostViewSet, basename='api-post')
router.register(r'category', CategoryViewSet, basename='api-category')

urlpatterns = [
    url(r'demo/$', demo, name='demo'),
    url(r'demo-list/$', demo_list, name='demo-list'),
    # path('admin/', admin.site.urls),
    # url(r'^$', post_list, name='index'),
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^category/(?P<category_id>\d+)/$', post_list, name='category-list'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    # url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    # url(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author-list'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),

    # url(r'^api/post/', post_list, name='post-list'),
    # url(r'^api/post/', PostList.as_view(), name='post-list'),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),
]
