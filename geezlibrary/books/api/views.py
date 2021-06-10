from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from books.api.permissions import IsCreatorOrReadOnly
from books.api.serializers import BorrowHistorySerializer, BookSerializer
from books.models import Book, BorrowHistory


class BorrowHistoryCreateAPIView(generics.CreateAPIView):
    """Allow users to register borrowing history for a book instance if it is available."""
    queryset = BorrowHistory.objects.all()
    serializer_class = BorrowHistorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        book = get_object_or_404(Book, slug=kwarg_slug)

        if  book.borrowHistories.filter(returned_date__isnull = True ).exists():
            raise ValidationError("This Book Is not Avaialble!")

        serializer.save(created_by=request_user, book=book)


class BorrowHistoryListAPIView(generics.ListAPIView):
    """Provide the borrowing history queryset of a specific book instance."""
    serializer_class = BorrowHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return BorrowHistory.objects.filter(book__slug=kwarg_slug).order_by("-created_at")


class BorrowHistoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for an borrow history instance to it's creator."""
    queryset = BorrowHistory.objects.all()
    serializer_class = BorrowHistorySerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Book."""
    queryset = Book.objects.all().order_by("title")
    lookup_field = "slug"
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]

    def get_queryset(self):
        query_set = self.queryset
        is_available = self.request.query_params.get('is_available')
        if is_available is not None:
            query_set = self.queryset.filter(is_available=is_available)
        
        
        return query_set
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    