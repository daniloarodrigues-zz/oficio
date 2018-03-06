from django.contrib import admin

# Register your models here.
from oficio.models import Orgao, Setor,Cargo, Responsavel, Oficio

admin.site.register(Orgao)
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(Responsavel)
admin.site.register(Oficio)
