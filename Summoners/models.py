from django.db import models

# Create your models here.

class Summoner(models.Model):
	name = models.CharField(max_length=200)
	internalName = models.CharField(max_length=200)
	acctId = models.IntegerField()
	profileIconId = models.IntegerField()
	revisionId = models.IntegerField()
	summonerLevel = models.IntegerField()
	summonerId = models.IntegerField()
	dataVersion = models.IntegerField()
	