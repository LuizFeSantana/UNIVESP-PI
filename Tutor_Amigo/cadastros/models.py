from django.db import models

# Create your models here.

class Animal(models.Model):
    idAnimal = models.AutoField(auto_created = True,primary_key = True,serialize = False)
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

    def _str_(self):
        return "{} ({})".format(self.Nome, self.especie)



class Usuario(models.Model):
    idUsuario = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    funcao = models.CharField(max_length=45, verbose_name='Função')
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    rg = models.CharField(max_length=9, verbose_name='RG')
    endereco = models.CharField(max_length=45, verbose_name='Endereço')
    email = models.CharField(max_length=45)

    idAnimal = models.OneToOneField('Animal', on_delete=models.CASCADE)

    def _str_(self):
        return "{} ({})".format(self.Nome, self.cpf)


class Ongs(models.Model):
    idOngs = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    razaosocial = models.CharField(max_length=45, verbose_name='Razão Social')
    email = models.CharField(max_length=45)
    resp = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45, verbose_name='Endereço')

    idAnimal = models.OneToOneField('Animal', on_delete=models.CASCADE)

    def _str_(self):
        return "{} - {} ({})".format(self.RazaoSocial, self.resp, self.CNPJ)

class Servicos(models.Model):
    idServicos = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    Petshop = models.CharField(max_length=45)
    AnimaisPerdidos = models.CharField(max_length=45)
    lartemporario = models.CharField(max_length=45)
    voluntarios = models.CharField(max_length=45)
    lardefinitivo = models.CharField(max_length=45)
    doadoresrecurso = models.CharField(max_length=45)
    taxidog = models.CharField(max_length=45)
    servveterinaio = models.CharField(max_length=45)

    idClinica = models.OneToOneField('Clinica', on_delete=models.CASCADE)

class Veterinario(models.Model):
    idVeterinario = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    nome = models.CharField(max_length=45)
    crmv = models.IntegerField()
    celular = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)

    idClinica = models.OneToOneField('Clinica', on_delete=models.CASCADE)

    def _str_(self):
        return "{} ({})".format(self.Nome, self.CRMV)

class Clinica(models.Model):
    idClinica = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    razaosocial = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=14)
    medicoresp = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)

    idServicos = models.OneToOneField('Servicos', on_delete=models.CASCADE)

    def _str_(self):
        return "{} ({})".format(self.RazaoSocial, self.CNPJ)

class Localizacao(models.Model):
    idLocalizacao = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    nome = models.CharField(max_length=45)
    logradouro = models.CharField(max_length=45)
    numero = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    cep = models.CharField(max_length=45)
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)
    localizacaocol = models.CharField(max_length=45)

    idClinica = models.OneToOneField('Clinica', on_delete=models.CASCADE)


class LarDefinitivo(models.Model):
    idLarDefinitivo = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    funcao = models.CharField(max_length=45)
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    endereco = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

    idUsuario = models.OneToOneField('Usuario', on_delete=models.CASCADE)

class LarTemporario(models.Model):
    idLarTemporario = models.AutoField(auto_created = True,primary_key = True,serialize = False)
    tutor = models.CharField(max_length=45)
    voluntario = models.CharField(max_length=45)
    petshop = models.CharField(max_length=45)
    clinicaveterinaria = models.CharField(max_length=45)

    idUsuario = models.OneToOneField('Usuario', on_delete=models.CASCADE)