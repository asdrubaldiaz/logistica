from django import forms
from .models import Cases

class CasesForm(forms.ModelForm):
	
	deadline =forms.DateField(widget=forms.TextInput(
		attrs={'type': 'date'}))
	fecha_cotizacion =forms.DateField(widget=forms.TextInput(
		attrs={'type': 'date'}))
	
	
	class Meta:
		
		model = Cases
		labels={"text":"Comentarios"}
		raw_id_fields = ("status",)
		fields = ('referencia', 'cliente','mv', 'deadline',  'status', 'numero_cotizacion','fecha_cotizacion','monto_cotizacion','ubicacion', 'text') 
