from django.contrib import admin
from .models import *

class ImagenesInLine(admin.TabularInline):
    model = Apartamento.imagen.through
    

#class Historia_medicaAdmin(admin.ModelAdmin):
#    inlines = [HistoriaAperturaAdultosInLine,]

class EdificioAdmin(admin.ModelAdmin):
    inlines = [ImagenesInLine,]

    exclude = ()


admin.site.register(Constructora)
admin.site.register(Edificio)
admin.site.register(Apartamento , EdificioAdmin)
admin.site.register(Imagenes)

