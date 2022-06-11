from django.db import models

# Create your models here.

class sanctuary(models.Model):
    Donar_name=models.CharField(max_length=30)
    Animal_name=models.CharField(max_length=30)
    age=models.CharField(max_length=40)
    weight=models.CharField(max_length=40)
    phoneno_of_donar=models.CharField(max_length=40)
    email_of_donar=models.EmailField()
    def __str__(self):
        return self.Donar_name
