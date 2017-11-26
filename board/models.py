from django.db import models
from django.utils import timezone

# Create your models here.

class Entregas(models.Model):
	entrega = models.AutoField(primary_key=True)
	author = models.ForeignKey('auth.User')
	barco = models.CharField(max_length=50)
	fecha_entrega =models.DateField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	hora_entrega = models.TimeField(default = '00:00', blank=True)
	entregador= models.ForeignKey( 'board.Entregadores', related_name = 'responsable', null = True)
	status = models.ForeignKey('board.Status', related_name = 'status', null = True)
	ubicacion = models.ForeignKey('board.Ubicacion', related_name = 'ubicacion', null = True)
	notas = models.CharField(default = 'notasviejas', max_length=100)
	agencia = models.ForeignKey('board.Agencia', related_name = 'status', null = True)
	sogas= models.BooleanField(default=False)
	pinturas= models.BooleanField(default=False)
	

	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self .barco
		
class Entregadores(models.Model):
	nombre = models.CharField(max_length=50)
	telefono = models.CharField(max_length=30)
	correo = models.CharField(max_length=30)
	activo = models.BooleanField(default=False)
	
	def publica(self):
		self.activo = True
		self.save()
		
	def __str__(self):
		return self.nombre
		
class Status(models.Model):
	nombre = models.CharField(max_length =50)
	
	def publica(self):
		self.save()
	
	def __str__(self):
		return self.nombre

class Ubicacion(models.Model):
	nombre = models.CharField(max_length =50)
	
	def publica(self):
		self.activo = True
		self.save()
	
	def __str__(self):
		return self.nombre
		
class Comment(models.Model):
    entrega = models.ForeignKey('board.Entregas', related_name='comments')
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Agencia(models.Model):
	nombre = models.CharField(max_length=50)
	contacto = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)
	correo =  models.CharField(max_length=50)

	def publica(self):
		self.save()

	def __str__(self):
		return self.nombre
		
class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
		
		

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')	
	
class Barcos(models.Model):
	nombre = models.CharField(max_length =50)
	
	def publica(self):
		self.activo = True
		self.save()
	
	def __str__(self):
		return self.nombre


