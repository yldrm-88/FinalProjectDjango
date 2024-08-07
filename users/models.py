from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name


class basvur(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=15)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.name