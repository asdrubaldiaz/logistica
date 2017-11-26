from django.db import models
from django.utils import timezone

# Create your models here.

class Cases(models.Model):
	case = models.AutoField(primary_key=True)
	cliente = models.CharField(max_length=100, default ='')
	referencia = models.CharField(max_length=50)
	author = models.ForeignKey('auth.User')
	barco =  models.ForeignKey('board.Barcos', related_name = 'barcos_entrega', null = True)
	mv = models.CharField(max_length=100, default='')
	deadline =models.DateField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	status = models.ForeignKey('followup.Status', related_name = 'status', null = True)
	ubicacion = models.ForeignKey('board.Ubicacion', related_name = 'ubicacion_entrega', null = True)
	notas = models.CharField(default = '', max_length=100)
	sogas= models.BooleanField(default=False)
	pinturas= models.BooleanField(default=False)
	comida = models.BooleanField(default=False)
	tecnico = models.BooleanField(default=False)
	bonded_stores = models.BooleanField(default=False)
	otros= models.BooleanField(default=False)
	fecha_cotizacion =  models.DateTimeField(blank=True, null=True)
	monto_cotizacion = models.DecimalField(max_digits=12, decimal_places=2)
	numero_cotizacion = models.IntegerField(blank = True, null = True)
	text = models.TextField(default = '')
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self .referencia

	
class Socios(models.Model):
	socio=  models.AutoField(primary_key=True)
	nombre_socio = models.CharField(max_length=50)
	contacto = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	correo = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	lista_de_precio = models.CharField(max_length=50)
	atendido_por = models.CharField(max_length=50)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	

class Status(models.Model):
	nombre = models.CharField(max_length =50)
	
	def publica(self):
		self.save()
	
	def __str__(self):
		return self.nombre