from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StorageProviderViewSet

router = DefaultRouter()
router.register(r'storage', StorageProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
