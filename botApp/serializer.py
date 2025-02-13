from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def validate_fecha_nacimiento(self, value):
        if value:
            formatos_fecha = [
                "%d/%m/%Y",  # dd/mm/yyyy
                "%d-%m-%Y",  # dd-mm-yyyy
                "%d %B %Y",  # 12 noviembre 1990
                "%d de %B de %Y",  # 12 de noviembre de 1990
                "%d %m %Y",
                "%d de %B %Y",
                "%d/%m/%y", 
                "%d-%m-%y",
                "%d %m %y"


            ]

            for formato in formatos_fecha:
                try:
                    # Intentamos convertir la fecha al formato DateField
                    datetime.strptime(value, formato).date()
                    return value  # Retornamos el valor si es válido
                except ValueError:
                    continue

            raise serializers.ValidationError("Formato de fecha inválido. Usa dd/mm/yyyy, dd-mm-yyyy, o 'día de mes de año'.")
        return value
        
class UsuarioRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRespuesta
        fields = "__all__"
        
class UsuarioTextoPreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioTextoPregunta
        fields = "__all__"
        
class MensajeContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensajeContenido
        fields = "__all__"

class UsuarioRespuestaFRNMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespUsuarioFactorRiesgoNoMod
        fields = "__all__"

class UsuarioRespuestaFRMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespUsuarioFactorRiesgoMod
        fields = "__all__"

class UsuarioRespuestaDSSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespDeterSalud
        fields = "__all__"