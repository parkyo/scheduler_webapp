from django.db import models

class Input(models.Model):
    text = models.CharField(max_length=10)
