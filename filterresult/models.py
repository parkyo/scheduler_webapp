from django.db import models

class Section(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    days = models.DateTimeField()

    def __str__(self):
        return self.start_time

class Class(models.Model):
    name = models.CharField(max_length=10)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

