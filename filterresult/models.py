from django.db import models

class Day(models.Model):
    day = models.CharField(max_length=2)

    def __str__(self):
        return self.day


class Section(models.Model):
    num = models.TextField()
    start_time = models.FloatField()
    end_time = models.FloatField()
    days = models.ManyToManyField(Day, blank=True)

    def __str__(self):
        return self.num


class Class(models.Model):
    name = models.CharField(max_length=10)
    section = models.ManyToManyField(Section, blank=True)
    
    def __str__(self):
        return self.name


