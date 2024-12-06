from rest_framework.routers import DefaultRouter

from books import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r"books", views.BookViewset, basename="books")


urlpatterns = router.urls
