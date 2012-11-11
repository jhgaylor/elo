from django.db import models

# Create your models here.
class Champion(models.Model):
	name = models.CharField(max_length=200)
	epid = models.IntegerField(primary_key=True)