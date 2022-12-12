from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('books', BookAPI.as_view({'get': 'list'})),
    path('books_update/<int:pk>', BookAPI.as_view({'post': 'update'})),
    path('books_detail/<int:pk>', BookAPI.as_view({'get': 'retrieve'})),
    path('books_delete/<int:pk>', BookAPI.as_view({'get': 'destroy'})),
    path('books_create', CreateBook.as_view()),
    path('authors', AuthorAPI.as_view({'get': 'list'})),
    path('authors_update/<int:pk>', AuthorAPI.as_view({'post': 'update'})),
    path('authors_detail/<int:pk>', AuthorAPI.as_view({'get': 'retrieve'})),
    path('authors_delete/<int:pk>', AuthorAPI.as_view({'get': 'destroy'})),
]