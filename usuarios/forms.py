from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico", required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'affiliation', 'country', 'password1', 'password2')
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'affiliation': 'Afiliación',
            'country': 'País',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = (
            "Tu contraseña no puede ser muy similar a tu otra información personal. "
            "Debe contener al menos 8 caracteres. "
            "No puede ser una contraseña común. "
            "No puede ser completamente numérica."
        )
        self.fields['password2'].help_text = "Introduce la misma contraseña que antes, para verificación."

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'usuario'  # Asignar rol de 'usuario' por defecto
        if commit:
            user.save()
        return user