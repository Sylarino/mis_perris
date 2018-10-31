from django import forms

from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota

		fields = [
			'nombre',
			'raza',
            'sexo',
			'descripcion',
            'estado',
			'persona',
			
		]
		labels = {
			'nombre': 'Nombre',
			'raza': 'Raza',
            'sexo': 'Sexo',
			'descripcion': 'Descripcion',
            'estado' : 'Estado',
			'persona': 'Adoptante',
			
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'raza': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'estado' : forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			
		}