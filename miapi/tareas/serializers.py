from rest_framework import serializers
from .models import CuentaVista

class CuentaVistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaVista
        fields = [
            'id',
            'numero_cuenta',
            'nombre_titular',
            'apellido_paterno',
            'apellido_materno',
            'rut',
            'correo',
            'telefono',
            'saldo',
            'fecha_apertura',
        ]
        read_only_fields = ['id', 'fecha_apertura']

    def validate_rut(self, value):
        return value.upper().strip()