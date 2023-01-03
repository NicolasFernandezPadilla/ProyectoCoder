from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField('Nombre de la categoria', max_length=80, null = False, blank= False)
    estado = models.BooleanField('Categoria Activada/Categoria no Activada', default= True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add= True)

class Meta:
    verbose_name = 'Categoria' 
    verbose_name_plural = 'Categorias'

def __str__(self):
    return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key= True)
    nombres = models.CharField('Nombres del autor', max_length=80, null = False, blank= False)
    apellidos = models.CharField('Apellidos del autor', max_length=80, null = False, blank= False)
    email = models.EmailField('Correo Electronico', blank= False, null= False)
    estado = models.BooleanField('Autor Activo/No Activo', default= True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now= False, auto_now_add= True)

class Meta:
    verbose_name = 'Autor'
    verbose_name_plural = 'Autores'

def __str__(self):
    return "{0},{1}".format(self.apellidos, self.nombres)


class Posteo(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 25, blank= False, null= False)
    slug= models.CharField('Slug', max_length = 100, blank= False, null= False)
    descripcion = models.CharField('Descripcion', max_length= 130, blank= False, null= False)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posteos')
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now= False, auto_now_add= True)



