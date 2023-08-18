from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from sports_centers.views import CentroEsportivoViewSet

router = routers.DefaultRouter()
router.register(r'centros-esportivos', CentroEsportivoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

# djoser
urlpatterns += [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]
