from django.db import models
from django.urls import reverse

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    marca = models.CharField(max_length=50)
    estoque = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

    
    def get_absolute_url(self):
        return reverse('produto-lista')
    
    
    
    