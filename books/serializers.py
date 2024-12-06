from rest_framework import serializers

from books.models import Book, Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            # "user",
            "id",
            "title",
            "description",
            "is_recommended",
            "avg_rating",
            "created_at",
            "modified_at",
        ]
        read_only_fields = ["avg_rating", "created_at", "modified_at"]


class ToggleRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "is_recommended",
        ]
        read_only_fields = [
            # "user",
            "id",
            "title",
            "description",
            "avg_rating",
            "created_at",
            "modified_at",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "book",
            "user",
            "id",
            "rating",
            "review",
            "created_at",
            "modified_at",
        ]
        read_only_fields = [
            "created_at",
            "modified_at",
        ]
