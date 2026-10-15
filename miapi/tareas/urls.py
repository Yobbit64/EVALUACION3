from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuentaVistaViewSet

router = DefaultRouter()
router.register(r'cuentas', CuentaVistaViewSet, basename='cuentavista')

urlpatterns = [
    path('', include(router.urls)),
]