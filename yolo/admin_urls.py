from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import management.urls
import learning.urls

urlpatterns = [
    url(r'^', include(management.urls)),
    url(r'^', include(learning.urls)),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
