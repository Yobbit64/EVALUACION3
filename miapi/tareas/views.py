from rest_framework import viewsets, filters
from .models import CuentaVista
from .serializers import CuentaVistaSerializer

class CuentaVistaViewSet(viewsets.ModelViewSet):
    queryset = CuentaVista.objects.all()
    serializer_class = CuentaVistaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['numero_cuenta', 'rut', 'nombre_titular', 'apellido_paterno', 'correo']
    ordering_fields = ['fecha_apertura', 'saldo', 'apellido_paterno']