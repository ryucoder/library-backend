from django.contrib import admin

from books.models import Book, Review


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ["id"]

    list_display_links = ["title"]

    list_filter = ["is_recommended"]

    list_display = [
        "id",
        "title",
        "is_recommended",
        "user",
        "created_at",
        "modified_at",
    ]

    list_per_page = 25


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ["id"]

    list_display_links = ["book"]

    list_filter = []

    list_display = [
        "id",
        "book",
        "user",
        "rating",
        "created_at",
        "modified_at",
    ]

    list_per_page = 25
