from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    add=models.CharField(max_length=20)
    contact=models.IntegerField(max_length=10)


    def __str__(self):
        return self.fname