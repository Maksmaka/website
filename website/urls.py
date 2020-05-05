from django.contrib import admin
from django.urls import path, include

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('blogapi.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
