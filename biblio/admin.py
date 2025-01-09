from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import *

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nom','parent')
	ordering = ('parent','nom')


class UsuariAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            ("Dades acadèmiques", {
                'fields': ('centre','cicle','imatge'),
            }),
    )

class ExemplarsInline(admin.TabularInline):
	model = Exemplar
	extra = 1
	readonly_fields = ('pk',)
	fields = ('pk','registre','exclos_prestec','baixa')

class LlibreAdmin(admin.ModelAdmin):
	filter_horizontal = ('tags',)
	inlines = [ExemplarsInline,]
	search_fields = ('titol','autor','CDU','signatura','ISBN','editorial','colleccio')
	list_display = ('titol','autor','editorial')

admin.site.register(Usuari,UsuariAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Pais)
admin.site.register(Llengua)
admin.site.register(Llibre,LlibreAdmin)
admin.site.register(Revista)
admin.site.register(Dispositiu)
admin.site.register(Imatge)

admin.site.register(Centre)
admin.site.register(Cicle)
admin.site.register(Reserva)
admin.site.register(Prestec)
admin.site.register(Peticio)
