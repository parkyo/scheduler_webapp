from django.db import models

class Input(models.Model):
    text = models.CharField(max_length=10)

    def __str__(self):
        return self.text