from django.db import models

# Create your models here.
class Profile(models.Model):
	image = models.ImageField(upload_to = 'images/')
	name = models.CharField(max_length = 10)
	date_of_birth = models.DateField()
	adress = models.CharField(max_length = 100)

