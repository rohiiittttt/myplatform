from django.urls import path, include
from .views import (
    ProductListView,
    CreateProductView,
    ProductEditView,
    ProductDeleteView
)
path('api/products/', include('products.urls')),

urlpatterns = [
    path('all-products/', ProductListView.as_view(), name='all-products'),
    path('create-product/', CreateProductView.as_view(), name='create-product'),
    path('edit-product/<int:pk>/', ProductEditView.as_view(), name='edit-product'),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='delete-product'),
]
