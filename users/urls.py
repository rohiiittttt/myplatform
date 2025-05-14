from django.urls import path
from .views import LoginView, ProductListView, ProtectedView,  dashboard_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('', dashboard_view, name='dashboard'),
    
]
