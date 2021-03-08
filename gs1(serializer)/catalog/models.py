from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120)
    roll = models.IntegerField()
    city = models.CharField(max_length=120)

    def __str__(self): # __str__ for Python 3, __unicode__ for Python 2
        return self.name