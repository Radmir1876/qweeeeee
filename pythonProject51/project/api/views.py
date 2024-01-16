from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookList(generics.ListCreateAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer

# Create your views here.
