# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('crear-formulario/', views.crear_formulario, name='crear_formulario'),
#     path('lista_proyectos/', views.lista_proyectos, name='lista_proyectos'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    # otras urls...
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyectos/crear/', views.crear_instrumento, name='crear_instrumento'),  # Ruta para crear un nuevo instrumento
    path('proyectos/editar/<int:instrumento_id>/', views.editar_instrumento, name='editar_instrumento'),
    path('proyectos/eliminar/<int:instrumento_id>/', views.eliminar_instrumento, name='eliminar_instrumento'),
    
]
