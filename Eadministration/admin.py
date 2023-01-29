from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Pays)
admin.site.register(Consulat)
admin.site.register(AgentDiplomatique)
admin.site.register(Bureau)
admin.site.register(Officier)
admin.site.register(Maire)
admin.site.register(Personne)
admin.site.register(ActeNaissance)
admin.site.register(ActeMariage)
admin.site.register(ActeDeces)
admin.site.register(Registre)

