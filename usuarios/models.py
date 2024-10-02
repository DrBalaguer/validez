# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     ROLES = (
#         ('evaluador', 'Evaluador'),
#         ('administrador', 'Administrador'),
#         ('usuario', 'Usuario'),
#         ('configuracion', 'Configuración'),
#     )
#     role = models.CharField(max_length=50, choices=ROLES)

#     # Nuevos campos
#     first_name = models.CharField(max_length=30, verbose_name='Nombre')
#     last_name = models.CharField(max_length=30, verbose_name='Apellidos')
#     affiliation = models.CharField(max_length=100, verbose_name='Afiliación')
#     country = models.CharField(max_length=50, verbose_name='País')

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('evaluador', 'Evaluador'),
        ('administrador', 'Administrador'),
        ('usuario', 'Usuario'),
        ('configuración', 'Configuración'),
    )

    role = models.CharField(max_length=50, choices=ROLES, default='usuario')

    first_name = models.CharField(max_length=30, verbose_name='Nombre')
    last_name = models.CharField(max_length=30, verbose_name='Apellidos')
    affiliation = models.CharField(max_length=100, verbose_name='Afiliación')
    country = models.CharField(max_length=50, verbose_name='País')

    def __str__(self):
        return self.username
