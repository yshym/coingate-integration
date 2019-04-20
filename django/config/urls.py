from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from .views import HomeView


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('coingate/', include('coingate.urls', namespace='coingate')),
)
