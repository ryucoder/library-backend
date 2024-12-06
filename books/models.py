from django.db import models

from core.models import TimeStampedModel


class Book(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="contacts"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_recommended = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Review(TimeStampedModel):
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
    rating = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        unique_together = ["book", "user"]
