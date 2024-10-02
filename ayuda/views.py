from django.shortcuts import render

def ayuda(request):
    return render(request, 'ayuda/ayuda.html')  # Asegúrate de incluir la carpeta en la ruta
