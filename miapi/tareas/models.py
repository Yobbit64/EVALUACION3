from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from decimal import Decimal

rut_validator = RegexValidator(
    regex=r'^\d{7,8}-[\dkK]$',
    message='El RUT debe tener el formato 12345678-9 (sin puntos y con guion).'
)

class CuentaVista(models.Model):
    numero_cuenta = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name="Número de Cuenta"
    )
    nombre_titular = models.CharField(
        max_length=100, 
        verbose_name="Nombre Titular"
    )
    apellido_paterno = models.CharField(
        max_length=100, 
        verbose_name="Apellido Paterno"
    )
    apellido_materno = models.CharField(
        max_length=100, 
        verbose_name="Apellido Materno"
    )
    rut = models.CharField(
        max_length=12,
        unique=True, 
        validators=[rut_validator],
        verbose_name="RUT"
    )
    correo = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name="Correo Electrónico"
    )
    telefono = models.CharField(
        max_length=15, 
        verbose_name="Teléfono"
    )
    saldo = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=Decimal('0.00'), 
        validators=[MinValueValidator(Decimal('0.00'))],
        verbose_name="Saldo"
    )
    fecha_apertura = models.DateField(
        auto_now_add=True, 
        verbose_name="Fecha de Apertura"
    )

    class Meta:
        db_table = "Cuenta_Vista"
        ordering = ['-fecha_apertura', 'apellido_paterno']

    def __str__(self):
        return f"{self.numero_cuenta} - {self.nombre_titular} {self.apellido_paterno} ({self.rut})"