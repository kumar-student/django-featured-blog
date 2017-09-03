from django.conf.urls import url
from blog.views.index import index_view
from blog.views.create_article import create_article_view
from blog.views.update_article import update_article_view
from blog.views.articles_list import articles_list_view
from blog.views.article_detail import article_detail_view
from blog.views.delete_article import delete_article_view


urlpatterns = [
    url(r'^$',index_view,name='index-view'),
    url(r'^articles/create/$',create_article_view,name='create-article'),
    url(r'^articles/(?P<id>\d+)/update/$',update_article_view,name='update-article'),
    url(r'^articles/$',articles_list_view,name='articles-list'),
    url(r'^articles/(?P<id>\d+)/$',article_detail_view,name='article-detail'),
    url(r'^articles/(?P<id>\d+)/delete/$',delete_article_view,name='delete'),
]