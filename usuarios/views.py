
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # Asegúrate de importar logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'usuarios/home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Registro exitoso. ¡Bienvenido/a, {username}!")
                return redirect('home')
            else:
                messages.error(request, "No se pudo autenticar al usuario después del registro.")
        else:
            messages.error(request, "Por favor, corrija los errores en el formulario.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Nombre de usuario o contraseña incorrectos.")
        return super().form_invalid(form)
    
