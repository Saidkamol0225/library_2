from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookList(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'author']

    def get(self, request, pk=None):
        if pk:
            book = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.get_serializer(book)
        else:
            books = self.get_queryset()
            serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, pk):
        book = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        book = get_object_or_404(self.get_queryset(), pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
