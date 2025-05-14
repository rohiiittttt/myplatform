from django.urls import path
from .views import LoginView, ProductListView, ProtectedView,  dashboard_view, ProtectedView  

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('', dashboard_view, name='dashboard'),
    
]
