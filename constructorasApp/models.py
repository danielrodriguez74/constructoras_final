from django.db import models

class Imagenes(models.Model):

    nombre = models.CharField(max_length = 100)
    imagen = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.nombre

class Apartamento(models.Model):

    nombre = models.CharField(max_length= 100 , help_text="Ingresar un identificador para el apartamento - Nombre + Edificio al que pertenece")
    numero = models.CharField(max_length = 500, help_text = "Numero en el edificio" )
    alcobas = models.CharField(max_length=100 , help_text = "Breve despcripcion de las alcobas")
    baño = models.CharField(max_length=100 , help_text = "Breve despcripcion de los baños")
    garaje = models.BooleanField(default = False)
    terraza = models.BooleanField(default = False)
    comedor = models.BooleanField(default = False)
    cocina = models.BooleanField(default = False)
    estado = models.BooleanField(default = False)
    descripcion_general = models.TextField(max_length=500, blank = True)
    imagen = models.ManyToManyField(Imagenes , through= 'ImgApartamento')

    def __str__(self):
        return self.nombre + " Numero del apartamento: " +self.numero

class ImgApartamento(models.Model):
    id_img = models.ForeignKey(Imagenes, on_delete = models.CASCADE)
    id_apartamento = models.ForeignKey(Apartamento , on_delete = models.CASCADE)

class Edificio(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    numero_de_apartamentos = models.IntegerField()
    imagen = models.ImageField(upload_to = 'fotosEdificios/')
    apartamentos = models.ManyToManyField(Apartamento)
   

    def __str__(self):
        return self.nombre


class Constructora(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    edificios = models.ManyToManyField(Edificio)
    imagen = models.ImageField(upload_to = 'fotosConstructoras/')

    def __str__(self):
        return self.nombre