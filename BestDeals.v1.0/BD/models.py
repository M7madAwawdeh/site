from django.db import models

class Product(models.Model):
    c = models.TextField()
    keywords = models.TextField()

