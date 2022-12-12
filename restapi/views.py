from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from rest_framework.response import Response

from .permissions import AdminPermission
from .serializers import *
from .models import Book


def index(request):
    return render(request, 'index.html')


class BookAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AdminPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre', 'author__middle_name']


class AuthorAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [AdminPermission]


class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AdminPermission]

    def create(self, request, *args, **kwargs):
        item = BookSerializer(data=request.data)
        if Book.objects.filter(title=request.data.get('title'),
                               author=request.data.get('author'),
                               yearOfRel=request.data.get('yearOfRel'),
                               publisher=request.data.get('publisher')) and ('Переведена с другого языка' == request.data.get('genre') or 'Переиздание' == request.data.get('genre')):
            raise serializers.ValidationError(" У вас такое уже есть!")

        if item.is_valid():
            item.save()
            return Response('Книга Сохранена')
        else:
            return Response('Книга НЕ сохранена')