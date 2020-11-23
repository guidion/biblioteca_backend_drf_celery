"""
Biblioteca URL Configuration
"""
from django.urls import re_path
from biblioteca.views import (
    AuthorList, AuthorDetail,
    PublisherList, PublisherDetail,
    BookList, BookDetail,
)

app_name = 'biblioteca'

authors = [
  re_path(r'^authors/$', AuthorList.as_view()),
  re_path(r'^authors/(?P<pk>\d+)$', AuthorDetail.as_view()),
]

publishers = [
  re_path(r'^publishers/$', PublisherList.as_view()),
  re_path(r'^publishers/(?P<pk>\d+)$', PublisherDetail.as_view()),
]

books = [
  re_path(r'^books/$', BookList.as_view()),
  re_path(r'^books/(?P<pk>\d+)$', BookDetail.as_view()),
]


urlpatterns = authors + publishers + books
