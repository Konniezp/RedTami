from rest_framework import serializers
from .models import *
from datetime import datetime
from fuzzywuzzy import fuzz
from unidecode import unidecode 


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

        def validate_fecha_nacimiento(self, value):

            fecha_por_defecto = "01/01/1920"
            fecha_defecto_obj = datetime.strptime(fecha_por_defecto, "%d/%m/%Y").date() 

            if value:  
                meses_correctos = [
                    "enero", "febrero", "marzo", "abril", "mayo", "junio",
                    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
                ]

                # Normalizar el texto: convertir a minúsculas y eliminar acentos
                fecha_normalizada = unidecode(value.lower())

                # Reemplazar nombres de meses mal escritos
                for mes in meses_correctos:
                    palabras_fecha = fecha_normalizada.split()
                    for palabra in palabras_fecha:
                        puntaje = fuzz.ratio(palabra, mes)
                        if puntaje > 70:  # Umbral de similitud
                            fecha_normalizada = fecha_normalizada.replace(palabra, mes)

                # Formatos de fecha permitidos
                formatos_fecha = [
                    "%d/%m/%Y",  # dd/mm/yyyy
                    "%d-%m-%Y",  # dd-mm-yyyy
                    "%d %B %Y",  # 12 noviembre 1990
                    "%d de %B de %Y",  # 12 de noviembre de 1990
                    "%d %m %Y",  # dd mm yyyy
                    "%d/%m/%y",  # dd/mm/yy
                    "%d-%m-%y",  # dd-mm-yy
                    "%d %m %y",  # dd mm yy
                    "%d de %B del %Y",  # 12 de noviembre del 1990
                    "%d de %B del %y",  # 12 de noviembre del 90
                    "%d de %B %y",  # 12 de noviembre 90
                    "%d de %B %Y",  # 12 de noviembre 1990
                ]
                fecha_valida = False

                for formato in formatos_fecha:
                    try:
                        fecha_convertida = datetime.strptime(fecha_normalizada, formato).date()
                        fecha_valida = True
                        return fecha_convertida 
                    except ValueError:
                        continue

                if not fecha_valida:
                    return fecha_defecto_obj

            return fecha_defecto_obj
        
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