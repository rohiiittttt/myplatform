from django.urls import path, include
from .views import (
    login_page, register_page, dashboard_view,
    LoginView, RegisterView, ProtectedView, UserViewSet,
    products_page, create_product_view, LogoutView
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import messaging_page
from .views import orders_page
from .views import buyer_orders_view
from . import views
from .views import UpdateUserInfoView
from .views import settings_page
from .views import storage_page

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [

    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('dashboard/', dashboard_view, name='dashboard'),
     path('storage/', storage_page, name='storage_page'),


    path('api/login/', TokenObtainPairView.as_view(), name='login_api'),
    path('api/register/', RegisterView.as_view(), name='register_api'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/products/', include('products.urls')),
    path('api/protected/', ProtectedView.as_view(), name='protected_api'),
    path('api/update-user/', UpdateUserInfoView.as_view(), name='update_user_info'),


    path('chat/', messaging_page, name='messaging_page'),
    path('orders/seller/', orders_page, name='orders_page'),
    path('orders/buyer/', buyer_orders_view, name='buyer_orders_page'),
    path('buyer-products/', views.buyer_products_page, name='buyer_products_page'),
    path('products/', products_page, name='products_page'),
    path('create-product/', create_product_view, name='create_product'),
    path('settings/', settings_page, name='settings_page'),  # <-- for frontend
]
