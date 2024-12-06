from django.core.validators import MinLengthValidator

from django.db import models

from django.contrib.auth.models import AbstractUser

from core.models import TimeStampedModel

from users.managers import UserManager


class User(TimeStampedModel, AbstractUser):
    CONTACT_GENDER_CHOICES = [
        ("female", "female"),
        ("male", "male"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    email = models.EmailField("Email ID", unique=True)
    is_email_verified = models.BooleanField(default=False)

    mobile = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    is_mobile_verified = models.BooleanField(default=False)

    dob = models.DateField()
    gender = models.CharField(
        max_length=6, choices=CONTACT_GENDER_CHOICES, default="female"
    )

    # @property
    # def owners_business(self):
    #     business = "None"

    #     if self.employer:
    #         return self.employer.business

    #     return business

    # def get_business(self):
    #     business = None

    #     if self.user_type == "owner":
    #         business = self.business
    #     else:
    #         business = self.employer.business

    #     return business

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
