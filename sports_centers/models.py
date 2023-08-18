from django.db import models

class CentroEsportivo(models.Model):
  nome = models.CharField(max_length=100)
  cep = models.CharField(max_length=100)
  telefone = models.CharField(max_length=100)

class Quadra(models.Model):
  nome = models.CharField(max_length=100)
  CentroEsportivo = models.ForeignKey(CentroEsportivo, on_delete=models.CASCADE)

  def __str__(self):
    return self.nome

class Reserva(models.Model):
  data = models.DateField()
  quadra = models.ForeignKey(Quadra, on_delete=models.CASCADE)
  CentroEsportivo = models.ForeignKey(CentroEsportivo, on_delete=models.CASCADE)

