from django.db import models

class Postagem(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=120)
    conteudo = models.TextField()
    data_publicacao = models.DateField(auto_now_add=True)
