from django.db import models
from usuarios.models import CustomUser

class ProyectoValidacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    autor_responsable = models.CharField(max_length=255)  # Asegúrate de que este campo esté definido
    objetivo_general = models.TextField()
    objetivos_especificos = models.TextField()
    alcance = models.CharField(max_length=50, choices=[
        ('nacional', 'Nacional'),
        ('regional', 'Regional'),
        ('distrital', 'Distrital'),
        ('provincial', 'Provincial')
    ])
    aplicado_a = models.CharField(max_length=255)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class ItemInstrumento(models.Model):
    proyecto = models.ForeignKey(ProyectoValidacion, on_delete=models.CASCADE)
    tipo_item = models.CharField(max_length=50, choices=[
        ('checkbox', 'CheckBox'),
        ('radiobutton', 'RadioButton'),
        ('togglebutton', 'ToggleButton'),
        ('select', 'Select'),
        ('large_text', 'Large text'),
        ('short_text', 'Short text'),
        ('dropbutton', 'DropButton')
    ])
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.tipo_item}: {self.descripcion}"

from django.db import models

class Proyecto(models.Model):
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    estatus = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion


class Instrumento(models.Model):
    nombre = models.CharField(max_length=255)
    autor_responsable = models.CharField(max_length=255)
    objetivo_general = models.TextField()
    objetivos_especificos = models.TextField()
    alcance = models.CharField(max_length=50, choices=[('Nacional', 'Nacional'), ('Regional', 'Regional'), ('Distrital', 'Distrital'), ('Provincial', 'Provincial')])
    aplicado_a = models.CharField(max_length=255, choices=[
        ('Estudiantes', 'Estudiantes'), 
        ('Docentes', 'Docentes'), 
        ('Directores de centros', 'Directores de centros'), 
        ('Técnicos de educación', 'Técnicos de educación'), 
        ('Otros', 'Otros')])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=50, choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Validado', 'Validado')], default='Pendiente')
    # Almacena los ítems seleccionados
    items = models.TextField(blank=True, help_text="Lista de ítems seleccionados para el instrumento")

    def __str__(self):
        return self.nombre

