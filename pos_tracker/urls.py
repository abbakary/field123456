from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),

    # Main tracker routes at root URL
    path("", include(("tracker.urls", "tracker"), namespace="tracker")),

    # Same tracker routes also available under /tracker/
    path("tracker/", include(("tracker.urls", "tracker_alt"), namespace="tracker_alt")),

    # Django auth
    path("accounts/", include("django.contrib.auth.urls")),
]

# Serve static files in development
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
