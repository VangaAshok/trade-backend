from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"create_ideas", views.IdeaViewSet, "idea-detail")
router.register(r"get_ideas", views.IdeaListViewSet, "idea-list")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]
