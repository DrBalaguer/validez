from django import forms
from .models import Instrumento

class InstrumentoForm(forms.ModelForm):
    ITEMS_OPCIONES = [
        ('CheckBox', 'CheckBox'), 
        ('RadioButton', 'RadioButton'), 
        ('ToggleButton', 'ToggleButton'), 
        ('SelectButton', 'SelectButton'), 
        ('Large Text', 'Large Text'), 
        ('Short Text', 'Short Text'), 
        ('DropButton', 'DropButton')
    ]

    items_seleccionados = forms.MultipleChoiceField(
        choices=ITEMS_OPCIONES, 
        widget=forms.CheckboxSelectMultiple,
        label="Selecciona los ítems"
    )

    class Meta:
        model = Instrumento
        fields = ['nombre', 'autor_responsable', 'objetivo_general', 'objetivos_especificos', 'alcance', 'aplicado_a', 'items_seleccionados']

    def save(self, commit=True):
        instrumento = super().save(commit=False)
        # Guarda los ítems seleccionados como una cadena separada por comas
        instrumento.items = ','.join(self.cleaned_data['items_seleccionados'])
        if commit:
            instrumento.save()
        return instrumento
