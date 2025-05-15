from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Functional app routes
    path('api/users/', include('users.urls')),
    path('api/products/', include('products.urls')),
    path('api/storage/', include('storage.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/messaging/', include('messaging.urls')),
    path('api/inventory/', include('inventory.urls')),

    # UI pages
    path('', include('users.urls')),  # for /login, /register, /dashboard etc.
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
