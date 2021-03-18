from django.contrib import admin
from core.models import Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'whatsapp', 'twitter', 'facebook', 'instagram', 'tiktok')

admin.site.register(Contato, ContatoAdmin)