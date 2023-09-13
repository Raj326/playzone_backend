import requests
from django.db import models
from django.conf import settings

token = "Bearer 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"

class CentroEsportivo(models.Model):
  dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  nome = models.CharField(max_length=100)
  endereco = models.CharField(max_length=100)
  telefone = models.CharField(max_length=100)
  imagem = models.ImageField(upload_to='centro_esportivo')
  latitude = models.FloatField()
  longitude = models.FloatField()
  resumo_comentarios = models.TextField(blank=True)

class TipoEsporte(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome

class Quadra(models.Model):
  centro_esportivo = models.ForeignKey(CentroEsportivo, on_delete=models.CASCADE)
  nome = models.CharField(max_length=100)
  tipos_esporte = models.ManyToManyField(TipoEsporte)
  imagem = models.ImageField(upload_to='quadra')

  def __str__(self):
    return self.nome

class Comentario(models.Model):
    centro_esportivo = models.ForeignKey(CentroEsportivo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return f"Comentário por {self.usuario.username} em {self.centro_esportivo.nome}"
  
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Atualizar o resumo dos comentários da quadra
        comentarios = Comentario.objects.filter(centro_esportivo=self.centro_esportivo)
        resumo_comentarios = ""

        for comentario in comentarios:
            resumo_comentarios += comentario.comentario + " "

        # Fazer a requisição para a API do OpenAI
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": token
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Pode me resumir esses comentários de uma quadra esportiva?" + resumo_comentarios}]
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            # Atualizar o resumo dos comentários da quadra com a resposta da API
            self.centro_esportivo.resumo_comentarios = response.json()["choices"][0]["message"]["content"]
            self.centro_esportivo.save()

class Reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quadra = models.ForeignKey(Quadra, on_delete=models.CASCADE)
    data = models.DateTimeField()

    def __str__(self):
        return f"Reserva de {self.usuario.username} para {self.quadra.nome} em {self.data}"