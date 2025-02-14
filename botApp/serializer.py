from rest_framework import serializers
from .models import *
from datetime import datetime
from fuzzywuzzy import process
from unidecode import unidecode 


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def validate_fecha_nacimiento(self, value):
        if value:
        # Lista de nombres de meses en español
            meses_correctos = [
                "enero", "febrero", "marzo", "abril", "mayo", "junio",
                "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
            ]

            # Normalizar el texto: convertir a minúsculas y eliminar acentos
            value_normalizado = unidecode(value.lower())

            # Reemplazar nombres de meses mal escritos
            for mes in meses_correctos:
                # Buscar coincidencias aproximadas
                coincidencia, puntaje = process.extractOne(mes, [value_normalizado])
                if puntaje > 80:  # Umbral de similitud (ajusta según sea necesario)
                    value_normalizado = value_normalizado.replace(coincidencia, mes)

            # Formatos de fecha permitidos
            formatos_fecha = [
                "%d/%m/%Y",  # dd/mm/yyyy
                "%d-%m-%Y",  # dd-mm-yyyy
                "%d %B %Y",  # 12 noviembre 1990
                "%d de %B de %Y",  # 12 de noviembre de 1990
                "%d %m %Y",  # dd mm yyyy
                "%d de %B %Y",  # 12 de noviembre 1990
                "%d/%m/%y",  # dd/mm/yy
                "%d-%m-%y",  # dd-mm-yy
                "%d %m %y",  # dd mm yy
                "%d de %B del %Y",  # 12 de noviembre del 1990
                "%d de %B del %y",  # 12 de noviembre del 90
            ]

            for formato in formatos_fecha:
                try:
                    # Intentamos convertir la fecha al formato DateField
                    datetime.strptime(value_normalizado, formato).date()
                    return value  # Retornamos el valor si es válido
                except ValueError:
                    continue

            raise serializers.ValidationError(
                "Formato de fecha inválido. Usa dd/mm/yyyy, dd-mm-yyyy, o 'día de mes de año'."
            )
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