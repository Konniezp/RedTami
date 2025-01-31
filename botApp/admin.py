from django.contrib import admin
from .models import *


class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "id_manychat",
        "Rut",
        "Whatsapp",
        "Referencia",
        "AnioNacimiento",
        "Comuna_Usuario",
        "Genero_Usuario",
        "SistemaSalud_Usuario",
        "Ocupacion_Usuario",
        "Fecha_Ingreso",
        "edad"
    )
    search_fields = (
        "id",
        "id_manychat",
        "Rut",
        "Whatsapp",
        "Referencia",
        "AnioNacimiento",
        "Comuna_Usuario",
        "Genero_Usuario",
        "SistemaSalud_Usuario",
        "Ocupacion_Usuario",
        "Fecha_Ingreso",
    )
    list_filter = (
        "id",
        "id_manychat",
        "Rut",
        "Whatsapp",
        "Referencia",
        "AnioNacimiento",
        "Comuna_Usuario",
        "Genero_Usuario",
        "SistemaSalud_Usuario",
        "Ocupacion_Usuario",
        "Fecha_Ingreso",
    )


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ("id", "pregunta")
    search_fields = ("id", "pregunta")
    list_filter = ("id", "pregunta")


class UsuarioRespuestaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "Rut",
        "id_opc_respuesta",
        "fecha_respuesta",
    )
    search_fields = (
        "id",
        "Rut",
        "id_opc_respuesta",
        "fecha_respuesta",
    )
    list_filter = (
        "id",
        "Rut",
        "id_opc_respuesta",
        "fecha_respuesta",
    )


class PreguntaOpcionRespuestaAdmin(admin.ModelAdmin):
    list_display = ("id", "id_pregunta", "OPC_Respuesta")
    search_fields = ("id", "id_pregunta", "OPC_Respuesta")
    list_filter = ("id", "id_pregunta", "OPC_Respuesta")


class ComunaAdmin(admin.ModelAdmin):
    list_display = ("id", "Nombre_Comuna")
    search_fields = ("id", "Nombre_Comuna")
    list_filter = ("id", "Nombre_Comuna")


class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "OPC_Genero")
    search_fields = ("id", "OPC_Genero")
    list_filter = ("id", "OPC_Genero")


class SistemaSaludAdmin(admin.ModelAdmin):
    list_display = ("id", "OPC_SistemaSalud")
    search_fields = ("id", "OPC_SistemaSalud")
    list_filter = ("id", "OPC_SistemaSalud")


class OcupacionAdmin(admin.ModelAdmin):
    list_display = ("id", "OPC_Ocupacion")
    search_fields = ("id", "OPC_Ocupacion")
    list_filter = ("id", "OPC_Ocupacion")


class UsuarioTextoPreguntaAdmin(admin.ModelAdmin):
    list_display = ("id", "Rut", "texto_pregunta", "fecha_pregunta")
    search_fields = ("id", "Rut", "texto_pregunta", "fecha_pregunta")
    list_filter = ("id", "Rut", "texto_pregunta", "fecha_pregunta")
    
class MensajeContenidoAdmin(admin.ModelAdmin):
    list_display = ("id", "texto", "Genero_Usuario","fecha")
    search_fields = ("id", "texto", "fecha", "Genero_Usuario")
    list_filter = ("id", "texto", "fecha", "Genero_Usuario")

class ultima_mamografia_anioAdmin(admin.ModelAdmin):
    list_display = ("id", "Rut", "anio_ult_mamografia","tiempo_transc_ult_mamografia")
    search_fields = ("id", "Rut", "anio_ult_mamografia","tiempo_transc_ult_mamografia")
    list_filter = ("id", "Rut", "anio_ult_mamografia","tiempo_transc_ult_mamografia")

class regionAdmin(admin.ModelAdmin):
    list_display =("id", "cod_region", "nombre_region")
    search_fields=("id", "cod_region", "nombre_region")
    list_filter=("id", "cod_region", "nombre_region")

class provinciaAdmin(admin.ModelAdmin):
    list_display=("id", "cod_provincia", "nombre_provincia", "cod_region")
    search_fields=("id", "cod_provincia", "nombre_provincia", "cod_region")
    list_filter=("id", "cod_provincia", "nombre_provincia", "cod_region")

class comuna_chileAdmin(admin.ModelAdmin):
    list_display=("id", "cod_comuna", "nombre_comuna", "cod_provincia")
    search_fields=("id", "cod_comuna", "nombre_comuna", "cod_provincia")
    list_filter=("id", "cod_comuna", "nombre_comuna", "cod_provincia")


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(UsuarioRespuesta, UsuarioRespuestaAdmin)
admin.site.register(PreguntaOpcionRespuesta, PreguntaOpcionRespuestaAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(SistemaSalud, SistemaSaludAdmin)
admin.site.register(Ocupacion, OcupacionAdmin)
admin.site.register(UsuarioTextoPregunta, UsuarioTextoPreguntaAdmin)
admin.site.register(MensajeContenido, MensajeContenidoAdmin)
admin.site.register(ultima_mamografia_anio, ultima_mamografia_anioAdmin)
admin.site.register(region, regionAdmin)
admin.site.register(provincia, provinciaAdmin)
admin.site.register(comuna_chile, comuna_chileAdmin)