from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from projects.views import signup_view
from django.contrib import admin
from django.urls import path, include
# Add this import for i18n_patterns
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from projects.views import signup_view
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

#
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('projects.urls')),

)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
