from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=80)
    whatsapp = models.CharField(max_length=20)
    twitter = models.CharField(max_length=120)
    facebook = models.CharField(max_length=120)
    instagram = models.CharField(max_length=120)
    linkedin = models.CharField(max_length=120)
    tiktok = models.CharField(max_length=120)

    class Meta:
        db_table = 'contatos'

    def __str__(self):
        return self.nome