from django.contrib import admin
from .models import Entregas, Entregadores, Status, Ubicacion, Comment, Agencia, Barcos
# Register your models here.

admin.site.register(Entregas)
admin.site.register(Entregadores)
admin.site.register(Status)
admin.site.register(Ubicacion)
admin.site.register(Comment)
admin.site.register(Agencia)
admin.site.register(Barcos)


