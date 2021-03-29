from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=80)
    whatsapp = models.CharField(max_length=20, blank=True)
    twitter = models.CharField(max_length=120, blank=True)
    facebook = models.CharField(max_length=120, blank=True)
    instagram = models.CharField(max_length=120, blank=True)
    linkedin = models.CharField(max_length=120, blank=True)
    tiktok = models.CharField(max_length=120, blank=True)

    class Meta:
        db_table = 'contatos'

    def __str__(self):
        return self.nome