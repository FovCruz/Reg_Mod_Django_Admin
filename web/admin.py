from django.contrib import admin
from .models import Persona

# Register your models here.

#REGISTRO GENERICO (vista desde el panel "personas" )
#admin.site.register(Persona)

#REGISTRO PERSONALIZADO (vista desde el panel "personas" )
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','edad','email')
    search_fields = ('nombre', 'email')