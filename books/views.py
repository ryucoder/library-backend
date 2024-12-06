from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from books.models import Book, Review
from books.serializers import (
    BookSerializer,
    ToggleRecommendationSerializer,
    ReviewSerializer,
)
from core.utils import CommonUtil


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    authentication_classes = CommonUtil.get_authentication_classes()

    def get_queryset(self):
        queryset = Book.objects.all().order_by("-created_at")
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        context["action"] = self.action
        return context

    def get_serializer_class(self):
        if self.action == "toggle_recommendation":
            return ToggleRecommendationSerializer

        return BookSerializer

    @action(detail=True, methods=["post"])
    def toggle_recommendation(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            instance.is_recommended = serializer.validated_data["is_recommended"]
            instance.save()

        output_serializer = BookSerializer(instance)
        return Response(output_serializer.data, status=status.HTTP_200_OK)


class ReviewViewset(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    authentication_classes = CommonUtil.get_authentication_classes()

    def get_queryset(self):
        queryset = Review.objects.all().order_by("-created_at")
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        context["action"] = self.action
        return context
