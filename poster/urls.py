from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'poster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('srcform.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)