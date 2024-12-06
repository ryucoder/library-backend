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


# class ToggleRecommendationSerializer(serializers.Serializer):
#     is_recommended = serializers.BooleanField(default=False)

#     class Meta:
#         fields = [
#             "is_recommended",
#         ]


class ToggleRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "is_recommended",
        ]
        read_only_fields = [
            "user",
            "id",
            "title",
            "description",
            "avg_rating",
            "created_at",
            "modified_at",
        ]
