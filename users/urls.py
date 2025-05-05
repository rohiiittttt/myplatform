from django.urls import path
from .views import LoginView, ProductListView, ProtectedView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
