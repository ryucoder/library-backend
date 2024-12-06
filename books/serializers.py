from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "user",
            "id",
            "title",
            "description",
            "is_recommended",
            "avg_rating",
            "created_at",
            "modified_at",
        ]
        read_only_fields = ["avg_rating", "created_at", "modified_at"]
