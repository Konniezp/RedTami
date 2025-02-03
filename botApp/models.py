from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date



class Comuna(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Comuna")
    Nombre_Comuna = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_Comuna


class Genero(models.Model):
    FEMENINO = "Femenino"
    MASCULINO = "Masculino"
    OTRO = "Otro"

    GENERO_CHOICES = [
        (FEMENINO, "Femenino"),
        (MASCULINO, "Masculino"),
        (OTRO, "Otro"),
    ]

    id = models.AutoField(primary_key=True, verbose_name="ID Genero")
    OPC_Genero = models.CharField(max_length=50, choices=GENERO_CHOICES)

    def __str__(self):
        return self.OPC_Genero


class SistemaSalud(models.Model):
    FONASA = "Fonasa"
    ISAPRE = "Isapre"
    OTRO = "Otro"

    SISTEMA_SALUD_CHOICES = [
        (FONASA, "Fonasa"),
        (ISAPRE, "Isapre"),
        (OTRO, "Otro"),
    ]

    id = models.AutoField(primary_key=True, verbose_name="ID Sistema Salud")
    OPC_SistemaSalud = models.CharField(max_length=50, choices=SISTEMA_SALUD_CHOICES)

    def __str__(self):
        return self.OPC_SistemaSalud


class Ocupacion(models.Model):
    DUENIACASA = "Dueña de Casa"
    TRABAJADOR = "Trabajadora"
    OTRO = "Otro"

    OCUPACION_CHOICES = [
        (DUENIACASA, "Dueña de Casa"),
        (TRABAJADOR, "Trabajadora"),
        (OTRO, "Otro"),
    ]

    id = models.AutoField(primary_key=True, verbose_name="ID Ocupacion")
    OPC_Ocupacion = models.CharField(max_length=50, choices=OCUPACION_CHOICES)

    def __str__(self):
        return self.OPC_Ocupacion


class Usuario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Usuario")
    AnioNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    id_manychat = models.CharField(max_length=200)
    Rut = models.CharField(max_length=10)
    Whatsapp = models.CharField(max_length=200)
    Referencia = models.CharField(max_length=200)
    Comuna_Usuario = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    Genero_Usuario = models.ForeignKey(Genero, on_delete=models.CASCADE)
    SistemaSalud_Usuario = models.ForeignKey(SistemaSalud, on_delete=models.CASCADE)
    Ocupacion_Usuario = models.ForeignKey(Ocupacion, on_delete=models.CASCADE)
    Fecha_Ingreso = models.DateTimeField(default=timezone.now)
    edad = models.IntegerField(default=0)

    #Cálculo de edad por medio de la fecha actual y la fecha de nacimiento (AnioNacimiento)
    def calculo_edad (self):
        fecha_actual = date.today()
        edad =  fecha_actual.year - self.AnioNacimiento.year
        edad -= ((fecha_actual.month, fecha_actual.day) < (self.AnioNacimiento.month, self.AnioNacimiento.day))
        return edad
    
    #Guardar edad con método save
    def save(self, *args, **kwargs):
        self.edad = self.calculo_edad()  
        super().save(*args, **kwargs) #Llama al método save

    def __str__(self):
        return str(self.id)
    

class Pregunta(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Pregunta")
    pregunta = models.CharField(max_length=200)

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

    def __str__(self):
        return f"{self.Rut} - {self.texto_pregunta}"


class MensajeContenido(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Texto")
    texto = models.CharField(max_length=200)
    Genero_Usuario = models.ForeignKey(Genero, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha")

class ultima_mamografia_anio(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID de última mamografía")
    Rut = models.CharField(max_length=10)
    anio_ult_mamografia = models.IntegerField(default=0, verbose_name="Año de última mamografía")
    tiempo_transc_ult_mamografia = models.IntegerField(default=0, verbose_name="Tiempo transcurrido")

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
    id = models.AutoField (primary_key=True, verbose_name="ID región")
    cod_region = models.CharField(max_length=2)
    nombre_region = models.CharField(max_length=200)

    def __str__(self):
        return self.cod_region

class provincia(models.Model):
    id = models.AutoField (primary_key=True, verbose_name="ID provincia")
    cod_provincia = models.CharField(max_length=4)
    nombre_provincia = models.CharField(max_length=200)
    cod_region = models.ForeignKey(region,on_delete = models.CASCADE)

    def __str__(self):
        return self.cod_provincia

class comuna_chile(models.Model):
    id = models.AutoField (primary_key=True, verbose_name="ID comuna")
    cod_comuna = models.CharField(max_length=6)
    nombre_comuna = models.CharField (max_length=200)
    cod_provincia = models.ForeignKey (provincia, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre_comuna
    
class PregFactorRiesgoMod(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Factor de Riesgo Mod")
    pregunta_FRM = models.CharField(max_length=200)

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
    

class PregDeterSalud(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID Determinantes sociales salud")
    pregunta_DS = models.CharField(max_length=200)

    def _str_(self):
        return self.pregunta_DS
    
class OpcDeterSalud(models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID Opc determinantes salud")
    opc_respuesta_DS = models.CharField(max_length=200)
    id_pregunta_DS = models.ForeignKey(PregDeterSalud, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.id_pregunta_DS} - {self.opc_respuesta_DS}"
    
class RespDeterSalud (models.Model):
    id = models.AutoField(primary_key=True, verbose_name= "ID Resp determinante salud")
    Rut = models.CharField(max_length=10)
    respuesta_DS = models.ForeignKey(OpcDeterSalud, on_delete=models.CASCADE)
    fecha_respuesta = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.Rut} - {self.respuesta_DS}"
   

