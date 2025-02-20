from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, datetime
from dateutil import parser
from unidecode import unidecode 
from fuzzywuzzy import fuzz

import locale
import re

locale.setlocale(locale.LC_TIME, 'es_ES') 
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Usuario")
    id_manychat = models.CharField(max_length=200)
    Rut = models.CharField(max_length=10)
    AnioNacimiento = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    Whatsapp = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254, blank=True)
    Comuna_Usuario = models.ForeignKey('comuna', on_delete=models.CASCADE)
    Referencia = models.CharField(max_length=200)
    Fecha_Ingreso = models.DateTimeField(default=timezone.now)
    edad = models.IntegerField(default=0)
    fecha_nacimiento = models.CharField(max_length=30, null=True, blank=True)

    # Cálculo de edad por medio de la fecha actual y la fecha de nacimiento (AnioNacimiento)
    def calculo_edad(self):
        if self.AnioNacimiento:
            fecha_actual = date.today()
            edad = fecha_actual.year - self.AnioNacimiento.year
            edad -= ((fecha_actual.month, fecha_actual.day) < (self.AnioNacimiento.month, self.AnioNacimiento.day))
            return edad
        return 0

    # Validación y guardado de fecha en save()
    def save(self, *args, **kwargs):
        if self.fecha_nacimiento:  # Solo si fecha_nacimiento está presente
            # Lista de nombres de meses en español
            meses_correctos = [
                "enero", "febrero", "marzo", "abril", "mayo", "junio",
                "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
            ]

            # Normalizar el texto: convertir a minúsculas y eliminar acentos
            fecha_normalizada = unidecode(self.fecha_nacimiento.lower())

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
                "%d de %b %Y",  # 12 de nov 1990
                "%d de %b %y",  # 12 de nov 90
                "%d de %b del %Y",  # 12 de nov del 1990
                "%d de %b del %y"   # 12 de nov del 90
            ]

            fecha_valida = False

            for formato in formatos_fecha:
                try:
                    # Intentamos convertir la fecha al formato DateField
                    fecha_convertida = datetime.strptime(fecha_normalizada, formato).date()
                    self.AnioNacimiento = fecha_convertida  # Guardamos en AnioNacimiento
                    fecha_valida = True
                    break  # Salimos si se convierte correctamente
                except ValueError:
                    continue

            if not fecha_valida:
                raise ValidationError(
                    f"Formato de fecha inválido. Recibido: '{self.fecha_nacimiento}'. Usa dd/mm/yyyy, dd-mm-yyyy, o 'día de mes de año'."
                )

        # Calcula la edad si AnioNacimiento es válido
        self.edad = self.calculo_edad()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Rut} - {self.id}"
    
class Codigos_preg (models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID códigos preguntas")
    codigo_preguntas = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.codigo_preguntas
    
class Pregunta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Pregunta")
    pregunta = models.CharField(max_length=200)
    codigo_preguntas = models.ForeignKey(Codigos_preg, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.pregunta

class PreguntaOpcionRespuesta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Opcion Respuesta")
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    OPC_Respuesta = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id_pregunta} - {self.OPC_Respuesta}"

class UsuarioRespuesta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Usuario Respuesta")
    Rut = models.CharField(max_length=10)
    id_opc_respuesta = models.ForeignKey(PreguntaOpcionRespuesta, on_delete=models.CASCADE)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Rut} - {self.id_opc_respuesta}"

class UsuarioTextoPregunta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Texto Pregunta")
    Rut = models.CharField(max_length=10)
    texto_pregunta = models.CharField(max_length=200)
    fecha_pregunta = models.DateTimeField(auto_now_add=True)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.Rut} - {self.texto_pregunta}"


class MensajeContenido(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Texto")
    texto = models.CharField(max_length=200)
    opcrespFRNM = models.ForeignKey('RespUsuarioFactorRiesgoNoMod', on_delete=models.CASCADE)
    opcrespFRM = models.ForeignKey('RespUsuarioFactorRiesgoMod', on_delete= models.CASCADE)
    opcrespDS = models.ForeignKey('RespDeterSalud', on_delete= models.CASCADE)
    opcresTM =models.ForeignKey(UsuarioRespuesta, on_delete= models.CASCADE)
    opcresUS = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha")

    def __str__(self):
        return f"{self.opcrespFRNM} - {self.opcrespFRM} - {self.opcrespDS} - {self.opcresTM} - {self.opcresUS}"


class ultima_mamografia_anio(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID de última mamografía")
    Rut = models.CharField(max_length=10)
    anio_ult_mamografia = models.IntegerField(default=0, verbose_name="Año de última mamografía")
    tiempo_transc_ult_mamografia = models.IntegerField(default=0, verbose_name="Tiempo transcurrido")
    fecha_pregunta = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    # Función para calcular tiempo transcurrido desde la última mamografía
    def calculo_tiempo_transc_ult_mamografia(self):
        anio_actual = int(date.today().year)
        tiempo_transc_ult_mamografia = anio_actual - self.anio_ult_mamografia
        return tiempo_transc_ult_mamografia

    # Guardar tiempo transcurrido con método save
    def save(self, *args, **kwargs):
        self.tiempo_transc_ult_mamografia = self.calculo_tiempo_transc_ult_mamografia()
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.Rut} - {self.anio_ult_mamografia}"

class region(models.Model):
    cod_region = models.CharField(primary_key=True, verbose_name= "Cod region", max_length=2)
    nombre_region = models.CharField(max_length=200)

    def __str__(self):
        return self.cod_region

class provincia(models.Model):
    cod_provincia = models.CharField(primary_key=True, verbose_name= "Cod provincia", max_length=4)
    nombre_provincia = models.CharField(max_length=200)
    cod_region = models.ForeignKey(region,on_delete = models.CASCADE)

    def __str__(self):
        return self.cod_provincia

class comuna(models.Model):
    cod_comuna = models.CharField(primary_key=True, verbose_name="Cod comuna", max_length=6)
    nombre_comuna = models.CharField (max_length=200)
    cod_provincia = models.ForeignKey (provincia, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre_comuna
    
class PregFactorRiesgoMod(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Factor de Riesgo Mod")
    pregunta_FRM = models.CharField(max_length=200)
    codigo_preguntas = models.ForeignKey(Codigos_preg, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.pregunta_FRM

class OpcFactorRiesgoMod(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID Opc Riesgo Mod")
    opc_respuesta_FRM = models.CharField(max_length=200)
    id_pregunta_FRM = models.ForeignKey(PregFactorRiesgoMod, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_pregunta_FRM} - {self.opc_respuesta_FRM}"

class RespUsuarioFactorRiesgoMod (models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID Resp Riesgo Mod")
    Rut = models.CharField(max_length=10)
    respuesta_FRM = models.ForeignKey(OpcFactorRiesgoMod, on_delete=models.CASCADE)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Rut} - {self.respuesta_FRM}"

class PregFactorRiesgoNoMod(models.Model):
    id = models.AutoField(primary_key= True, verbose_name= "ID Factor de Riesgo No Mod")
    pregunta_FRNM = models.CharField(max_length=200)
    codigo_preguntas = models.ForeignKey(Codigos_preg, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.pregunta_FRNM

class OpcFactorRiesgoNoMod(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID Opc Riesgo No Mod")
    opc_respuesta_FRNM = models.CharField(max_length=200)
    id_pregunta_FRNM = models.ForeignKey(PregFactorRiesgoNoMod, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_pregunta_FRNM} - {self.opc_respuesta_FRNM}"

class RespUsuarioFactorRiesgoNoMod (models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID Resp Riesgo Mod")
    Rut = models.CharField(max_length=10)
    respuesta_FRNM = models.ForeignKey(OpcFactorRiesgoNoMod, on_delete=models.CASCADE)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Rut} - {self.respuesta_FRNM}"
    
class PregDeterSalud(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Determinantes sociales salud")
    pregunta_DS = models.CharField(max_length=200)
    codigo_preguntas = models.ForeignKey(Codigos_preg, on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.pregunta_DS
    
class OpcDeterSalud(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID Opc determinantes salud")
    opc_respuesta_DS = models.CharField(max_length=200)
    id_pregunta_DS = models.ForeignKey(PregDeterSalud, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_pregunta_DS} - {self.opc_respuesta_DS}"
    
class RespDeterSalud (models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID Resp determinante salud")
    Rut = models.CharField(max_length=10)
    respuesta_DS = models.ForeignKey(OpcDeterSalud, on_delete=models.CASCADE)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Rut} - {self.respuesta_DS}"
    
class RespTextoFRM(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID índice antropométrico")
    Rut = models.CharField(max_length=10)
    peso_FRM6 = models.CharField(max_length= 3)  # Peso en kg
    altura_FRM5 = models.CharField(max_length= 4)  # Altura en cm
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    id_usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.Rut} - Peso: {self.peso_FRM6} kg - Altura: {self.altura_FRM5} cm"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guardamos el dato bruto primero
        CalculoFRM.procesar_datos_brutos(self)  # Llamamos la limpieza

class CalculoFRM(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Cálculo FRM")
    Rut = models.CharField(max_length=10)
    altura_mod = models.FloatField(default=0)
    peso_mod = models.FloatField(default=0)
    imc = models.FloatField(default=0.0) 
    datos_originales = models.OneToOneField(RespTextoFRM, on_delete=models.CASCADE)

    def calculo_imc(self):
        if self.altura_mod > 0 and self.peso_mod > 0:  
            altura_metros = self.altura_mod / 100  # Convierte de cm a metros
            return round(self.peso_mod / (altura_metros ** 2), 2)  # Redondear a 2 decimales
        return 0.0  # Retorna 0 si la altura no es válida

    def save(self, *args, **kwargs):
        self.imc = self.calculo_imc() 
        super().save(*args, **kwargs)
    
    @staticmethod
    def limpiar_numero(valor, es_altura=False):
        if not valor:
            return 0.0

        # Diccionario para convertir palabras a números
        palabras_a_numeros = {
            'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4,
            'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9,
            'diez': 10, 'once': 11, 'doce': 12, 'trece': 13, 'catorce': 14,
            'quince': 15, 'dieciséis': 16, 'diecisiete': 17, 'dieciocho': 18,
            'diecinueve': 19, 'veinte': 20, 'treinta': 30, 'cuarenta': 40,
            'cincuenta': 50, 'sesenta': 60, 'setenta': 70, 'ochenta': 80,
            'noventa': 90, 'cien': 100
        }

        valor_lower = str(valor).strip().lower()
        if valor_lower in palabras_a_numeros:
            return palabras_a_numeros[valor_lower]

        # Limpieza de caracteres no numéricos
        valor = valor.strip().replace(',', '.')  # Espacios y comas → puntos
        valor = re.sub(r'[^0-9.]', '', valor)  # Quitar letras y símbolos

        partes = valor.split('.')
        if len(partes) > 2:
            valor = partes[0] + '.' + partes[1]  # Mantener solo el primer punto


        try:
            valor_numerico = float(valor)
            if es_altura and valor_numerico > 250:  
                valor_numerico /= 10  # Corrige alturas mal escritas (ej. "1700" → "170")
            return valor_numerico if valor_numerico > 0 else 0.0
        except ValueError:
            return 0.0

    @classmethod
    def procesar_datos_brutos(cls, instance):
        peso_formateado = cls.limpiar_numero(instance.peso_FRM6)
        altura_formateada = cls.limpiar_numero(instance.altura_FRM5, es_altura=True)
        
        formateado, created = cls.objects.get_or_create(
            datos_originales=instance,
            defaults={
                "Rut": instance.Rut,
                "peso": peso_formateado,
                "altura": altura_formateada,
            }
        )

        if not created:
            formateado.peso_mod= peso_formateado
            formateado.altura_mod= altura_formateada
            formateado.save()
    
      

