from django.db import models

# Create your models here.
class Cliente(models.Model):
  nome = models.CharField('nome', max_length=80)
  email = models.EmailField('email',unique=True)
  data_cadastro = models.DateTimeField('Data de Cadastro',auto_now_add=True)
  pontos = models.PositiveIntegerField('Ponto',default=0)
  avatar = models.URLField('Avatar(URL)', blank=True, null=True)

  def __str__(self):
    return self.nome