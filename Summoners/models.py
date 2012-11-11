from django.db import models
from Champions.models import Champion
# Create your models here.

class Summoner(models.Model):
	name 			= models.CharField(max_length=200)
	internalName 	= models.CharField(max_length=200)
	acctId 			= models.IntegerField(primary_key=True)
	profileIconId 	= models.IntegerField()
	revisionId 		= models.IntegerField()
	summonerLevel 	= models.IntegerField()
	summonerId 		= models.IntegerField()
	dataVersion 	= models.IntegerField()

class RankedChampionStats(models.Model):
	championId = models.ForeignKey(Champion)
    wins = models.IntegerField()
    losses = models.IntegerField()
    gamesPlayed	= models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    doubleKills	= models.IntegerField()
    tripleKills	= models.IntegerField()
    quadraKills	= models.IntegerField()
    pentaKills = models.IntegerField()
    maximumKills = models.IntegerField()
    maximumDeaths = models.IntegerField()
    minionKills = models.IntegerField()
    gold = models.IntegerField()
    turretsDestroyed = models.IntegerField()
    damageDealt = models.IntegerField()
    physicalDamageDealt	= models.IntegerField()
    magicalDamageDealt = models.IntegerField()
    damageTaken = models.IntegerField()
    timeSpentDead = models.IntegerField()