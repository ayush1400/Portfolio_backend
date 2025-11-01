from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),
]

# Add this - it's CRITICAL for serving uploaded files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)