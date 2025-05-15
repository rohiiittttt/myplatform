from django.urls import path
from .views import LoginView, ProtectedView  
from .views import RegisterView
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView 
from .views import LogoutView


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
