from rest_framework import serializers
from .models import *
from datetime import datetime
from fuzzywuzzy import fuzz
from unidecode import unidecode 
import re


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def validate_fecha_nacimiento(self, value):
        if value:
            # Diccionario de nombres de meses y sus abreviaturas en español
            meses_correctos = {
                "enero": ["ene"],
                "febrero": ["feb"],
                "marzo": ["mar"],
                "abril": ["abr"],
                "mayo": ["may"],
                "junio": ["jun"],
                "julio": ["jul"],
                "agosto": ["ago"],
                "septiembre": ["sep", "set"],
                "octubre": ["oct"],
                "noviembre": ["nov"],
                "diciembre": ["dic"]
            }

            # Normalizar el texto: convertir a minúsculas y eliminar acentos
            fecha_normalizada = unidecode(str(value).lower())

            # Reemplazar abreviaturas y nombres mal escritos
            palabras_fecha = re.findall(r'\b\w+\b', fecha_normalizada)
            for palabra in palabras_fecha:
                for mes, abreviaturas in meses_correctos.items():
                    # Verifica similitudes con el nombre completo del mes
                    puntaje = fuzz.ratio(palabra, mes)
                    if puntaje > 70:
                        fecha_normalizada = re.sub(rf'\b{palabra}\b', mes, fecha_normalizada)

                    # Verifica similitudes con las abreviaturas del mes
                    for abreviatura in abreviaturas:
                        puntaje_abrev = fuzz.ratio(palabra, abreviatura)
                        if puntaje_abrev > 80:  # Umbral más alto para abreviaturas
                            fecha_normalizada = re.sub(rf'\b{palabra}\b', mes, fecha_normalizada)

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
                    # Intentamos convertir la fecha al formato DateField
                    fecha_convertida = datetime.strptime(fecha_normalizada, formato).date()
                    fecha_valida = True
                    return fecha_convertida  # Retornamos la fecha convertida si es válida
                except ValueError:
                    continue

            if not fecha_valida:
                raise serializers.ValidationError(
                    f"Formato de fecha inválido. Recibido: '{value}'. Usa dd/mm/yyyy, dd-mm-yyyy, o 'día de mes de año'."
                )

        return value  # Retorna el valor si no hay fecha para validar    
        
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