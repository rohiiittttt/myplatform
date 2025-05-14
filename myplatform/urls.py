from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Include users app URLs
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include('users.urls')),
         path('api/', include('products.urls')),
             path('api/', include('storage.urls')),
               path('api/', include('orders.urls')),
               path('api/', include('messaging.urls')),
          path('api/', include('inventory.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
