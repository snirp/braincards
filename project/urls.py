from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest.router import router
from django.conf.urls.static import static

from cards.views import quiz_detail
from users.views import profile
from rest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', profile),
    path('accounts/', include('allauth.urls')),
    path('rest/quiz/<slug:shortname>/<slug:identifier>', quiz_detail),
    path('rest/', include(router.urls)),
    path('rest-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
