from django.db import models

# Create your models here.

class Product:
    id : int
    name : str
    desc : str
    img : str
    price : float