from rest_framework import viewsets

from books.models import Book
from books.serializers import BookSerializer
from core.utils import CommonUtil


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    authentication_classes = CommonUtil.get_authentication_classes()

    def get_queryset(self):
        queryset = Book.objects.all().order_by("-created_at")
        return queryset
