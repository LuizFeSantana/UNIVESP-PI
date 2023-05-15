from django.db import models

# Create your models here.

class Animais(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50, verbose_name="Espécie")
    idade = models.IntegerField()



class Usuario(models.Model):
    nome = models.CharField(max_length=255)


class Ongs(models.Model):
    razaosocial = models.CharField(max_length=255, verbose_name="Razão Social")

class Serviços(models.Model):
    petshop = models.CharField(max_length=255)

class Veterinario(models.Model):
    nome = nome = models.CharField(max_length=50)

class Clinica(models.Model):
    razaosocial = models.CharField(max_length=255, verbose_name="Razão Social")

class Localização(models.Model):
    nome = models.CharField(max_length=255)

class Lardefinitivo(models.Model):
    funcao = models.CharField(max_length=50, verbose_name="Função")

class Lartemporario(models.Model):
    Tutor = models.CharField(max_length=50)