from django.db import models

# Create your models here.

class Animais(models.Model):
    id_animal = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50, verbose_name='Espécie')
    raca = models.CharField(max_length=50, verbose_name='Raça')
    GENERO_CHOICES = (
        ('macho', 'macho'),
        ('fêmea', 'fêmea'),
    )
    genero = models.CharField(max_length=6, choices=GENERO_CHOICES, verbose_name='Gênero')
    idade = models.IntegerField()
    cor = models.CharField(max_length=50)
    CONDICAO_CHOICES = (
        ('saudável', 'saudável'),
        ('ferido', 'ferido'),
        ('doente', 'doente'),
    )
    condicao_de_saude = models.CharField(max_length=9, choices=CONDICAO_CHOICES, verbose_name='Condição de saúde')
    ESTERILIZADO_CHOICES = (
        ('sim', 'sim'),
        ('não', 'não'),
    )
    esterilizado = models.CharField(max_length=3, choices=ESTERILIZADO_CHOICES)
    data_ultimo_atendimento = models.DateField()
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

    idLarDefinitivo = models.ForeignKey('LarDefinitivo', on_delete=models.CASCADE)
    idLarTemporario = models.ForeignKey('LarTemporario', on_delete=models.CASCADE)
    idLocalizacao = models.ForeignKey('Localizacao', on_delete=models.CASCADE)




class Usuario(models.Model):
    idUsuario = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    Funcao = models.CharField(max_length=45, verbose_name='Função')
    Nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    rg = models.CharField(max_length=9, verbose_name='RG')
    endereco = models.CharField(max_length=45, verbose_name='Endereço')
    email = models.CharField(max_length=45)

    idAnimal = models.ForeignKey('Animais', on_delete=models.CASCADE)


class Ongs(models.Model):
    idOngs = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    RazaoSocial = models.CharField(max_length=45, verbose_name='Razão Social')
    email = models.CharField(max_length=45)
    resp = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    CNPJ = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45, verbose_name='Endereço')

    idAnimal = models.ForeignKey('Animais', on_delete=models.CASCADE)

class Servicos(models.Model):
    idServicos = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    Petshop = models.CharField(max_length=45)
    AnimaisPerdidos = models.CharField(max_length=45)
    LarTemporario = models.CharField(max_length=45)
    Voluntarios = models.CharField(max_length=45)
    larDefinitivo = models.CharField(max_length=45)
    DoadoresRecurso = models.CharField(max_length=45)
    TaxiDog = models.CharField(max_length=45)
    ServVeterinaio = models.CharField(max_length=45)

    idClinica = models.ForeignKey('Clinica', on_delete=models.CASCADE)

class Veterinario(models.Model):
    id_Veterinario = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    nome = models.CharField(max_length=45)
    CRMV = models.IntegerField()
    celular = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)

    idClinica = models.ForeignKey('Clinica', on_delete=models.CASCADE)

class Clinica(models.Model):
    idClinica = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    razaoSocial = models.CharField(max_length=45)
    CNPJ = models.CharField(max_length=14)
    medicoResp = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)

    idServicos = models.ForeignKey('Servicos', on_delete=models.CASCADE)

class Localizacao(models.Model):
    idLocalizacao = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    Nome = models.CharField(max_length=45)
    logradouro = models.CharField(max_length=45)
    numero = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)
    Localizacaocol = models.CharField(max_length=45)

    idClinica = models.ForeignKey('Clinica', on_delete=models.CASCADE)


class LarDefinitivo(models.Model):
    idLarDefinitivo = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    Funcao = models.CharField(max_length=45)
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    endereco = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

class LarTemporario(models.Model):
    idLarTemporario = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    Tutor = models.CharField(max_length=45)
    voluntario = models.CharField(max_length=45)
    PetShop = models.CharField(max_length=45)
    ClinicaVeterinaria = models.CharField(max_length=45)

    idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)