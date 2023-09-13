from django.contrib import admin
from .models import Quadra, CentroEsportivo, Reserva, Comentario, TipoEsporte

admin.site.register(Quadra)
admin.site.register(CentroEsportivo)
admin.site.register(Reserva)
admin.site.register(Comentario)
admin.site.register(TipoEsporte)
