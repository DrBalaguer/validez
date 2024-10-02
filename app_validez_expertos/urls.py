from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('proyectos/', include('proyectos.urls')),
    path('ayuda/', include('ayuda.urls')),
    path('', include('usuarios.urls')),  # Ruta para manejar el home y otras vistas de usuarios
    
    
]
