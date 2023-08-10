from django.db import models
import uuid

class Enterprises(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cnpj = models.CharField(max_length=20, unique=True)
    nome_razao = models.CharField(max_length=50)
    nome_fantasia = models.CharField(max_length=50, unique=True)
    cnae = models.CharField(max_length=255)
    

