from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password


TIPUS_MATERIAL_CHOICES = [
    ('llibre', 'Llibre'),
    ('joc','Joc'),
    ('revista','Revista'),
    ('CD', 'CD'),
    ('DVD', 'DVD'),
    ('BR', 'Blu-ray'),
    ('dispositiu', 'Dispositiu'),
]

class Pais(models.Model):
    nom = models.CharField(max_length=200)

class Llengua(models.Model):
    nom = models.CharField(max_length=200)

class Cataleg(models.Model):
    #tipus = models.CharField(max_length=100, choices=TIPOS_MATERIAL_CHOICES)
    titol = models.CharField(max_length=100)
    autor = models.CharField(max_length=200, blank=True, null=True)
    CDU = models.CharField(max_length=40)
    signatura = models.CharField(max_length=40)
    data_edicio = models.DateField(null=True,blank=True)
    resum = models.TextField(blank=True,null=True)
    anotacions = models.TextField(blank=True,null=True)
    mides = models.CharField(max_length=100,null=True,blank=True)
    def exemplars(self):
    	return 0

class Llibre(Cataleg):
    ISBN = models.CharField(max_length=13)
    editorial = models.CharField(max_length=100, blank=True, null=True)
    colleccio = models.CharField(max_length=100, blank=True, null=True)
    lloc = models.CharField(max_length=100, blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True)
    llengua = models.ForeignKey(Llengua, on_delete=models.SET_NULL, blank=True, null=True)
    numero = models.IntegerField(null=True,blank=True)
    volums = models.IntegerField(null=True,blank=True)
    pagines = models.IntegerField()

class Revista(Cataleg):
    ISSN = models.CharField(max_length=13)
    editorial = models.CharField(max_length=100, blank=True, null=True)
    #colleccio = models.CharField(max_length=100, blank=True, null=True)
    lloc = models.CharField(max_length=100, blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True)
    llengua = models.ForeignKey(Llengua, on_delete=models.SET_NULL, blank=True, null=True)
    numero = models.IntegerField(null=True,blank=True)
    volums = models.IntegerField(null=True,blank=True)
    pagines = models.IntegerField()

class CD(Cataleg):
    discografica = models.CharField(max_length=100)
    estil = models.CharField(max_length=100)
    duracio = models.TimeField()

class DVD(Cataleg):
    productora = models.CharField(max_length=100)
    duracio = models.IntegerField()

class BR(Cataleg):
    productora = models.CharField(max_length=100)
    duracio = models.IntegerField()

class Dispositiu(Cataleg):
    modelo = models.CharField(max_length=100, default="")
    serie = models.CharField(max_length=100, default="")

class Exemplar(models.Model):
    cataleg = models.ForeignKey(Cataleg, on_delete=models.CASCADE)
    identificador = models.CharField(max_length=100)
    exclos_prestec = models.BooleanField(default=True)
    baixa = models.BooleanField(default=False)

class Imatge(models.Model):
    cataleg = models.ForeignKey(Cataleg, on_delete=models.CASCADE)
    imatge = models.ImageField(upload_to='imatges/')


# Usuaris

"""class Centre(models.Model):
    nom = models.CharField(max_length=200)

class Cicle(models.Model):
    nom = models.CharField(max_length=200)

class Usuari(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default="") 
    nom = models.CharField(max_length=50, default="") 
    cognoms = models.CharField(max_length=100, default="") 
    data_naixement = models.DateField()
    centre = models.ForeignKey(Centre, on_delete=models.SET_NULL, null=True)
    cicle = models.ForeignKey(Cicle, on_delete=models.SET_NULL, null=True)
    imatge = models.ImageField(upload_to='imatges/', null=True, blank=True) 
    contrasenya_cifrada = models.CharField(max_length=128,default="")  # Longitud suficiente para almacenar la contraseña cifrada

class Reserva(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)

class Prestec(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
    data_prestec = models.DateField(auto_now_add=True)
    data_retorn = models.DateField(null=True, blank=True)
    anotacions = models.TextField(blank=True,null=True)

class Peticio(models.Model):
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    titol = models.CharField(max_length=200)
    descripcio = models.TextField()
    data = models.DateField(auto_now_add=True)

class Log(models.Model):
    TIPO_LOG = (
        ('INFO', 'Información'),
        ('WARNING', 'Advertencia'),
        ('ERROR', 'Error'),
        ('FATAL', 'Fatal'),
    )
    
    usuari = models.CharField(max_length=100, null=True, blank=True)
    accio = models.CharField(max_length=100)
    data_accio = models.DateTimeField(auto_now_add=True)
    tipus = models.CharField(max_length=10, choices=TIPO_LOG, default="")

    def __str__(self):
        return f"{self.accio} - {self.tipus}"

"""
