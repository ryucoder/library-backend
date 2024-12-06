from django.conf import settings

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CommonUtil:
    @staticmethod
    def get_authentication_classes():
        authentication_classes = []

        if settings.ENVIRONMENT != "production":
            authentication_classes.append(SessionAuthentication)
            authentication_classes.append(BasicAuthentication)

        return authentication_classes
