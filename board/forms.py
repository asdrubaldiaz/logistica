from django import forms
from .models import Entregas, Comment, Document

class EntregasForm(forms.ModelForm):
	barco = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
		}
	
	))

	fecha_entrega =forms.DateField(widget=forms.TextInput(
		attrs={'type': 'date'} 
	))
	class Meta:
		model = Entregas
		fields = ('entrega', 'barco', 'fecha_entrega', 'published_date', 'entregador', 'status', 'ubicacion', 'agencia' , 'sogas', 'pinturas')
		
class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('author', 'text',)
		

		
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )