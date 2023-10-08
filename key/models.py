from django.db import models

class Key(models.Model):
    key = models.CharField("Key para resgate (Recomendado 50 caracteres)", max_length=50)
    link = models.CharField("Recompensa", max_length=200)

    def __str__(self):
        return f'Key {self.key} Recompensa: {self.link}'
