from django.urls import path
from .views import (
    login_page, register_page, dashboard_view,
    LoginView, RegisterView, ProtectedView, UserViewSet
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import products_page
from .views import create_product_view

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # HTML pages
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_view, name='dashboard'),

    # API endpoints
    path('api/login/', TokenObtainPairView.as_view(), name='login_api'),
    path('api/register/', RegisterView.as_view(), name='register_api'),

    # Optional protected route (for testing token)
    path('api/protected/', ProtectedView.as_view(), name='protected_api'),
    path('products/', products_page, name='products_page'),
     path('create-product/', create_product_view, name='create_product'),
]
