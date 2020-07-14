from django.db import models

class Section(models.Model):
    num = models.CharField(max_length=5)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    days = models.CharField(max_length=5)

    def __str__(self):
        return self.num


class Class(models.Model):
    name = models.CharField(max_length=10)
    section = models.ManyToManyField(Section, blank=True)
    
    def __str__(self):
        return self.name


