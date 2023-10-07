from django.db import models

# Create your models here.\
class person(models.Model):
    name = models.CharField(max_length=60)
    phone = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name
    
class Adhar(models.Model):
    person = models.OneToOneField("person",on_delete=models.CASCADE)
    signature = models.TextField()
    adhar_no = models.TextField(max_length=20)
    def __str__(self):
        return str(self.person)
