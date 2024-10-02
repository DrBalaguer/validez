from django.urls import path
from . import views

urlpatterns = [
    path('', views.ayuda, name='ayuda'),  # Ahora la ruta base es simplemente '' para que funcione con /ayuda/
]
