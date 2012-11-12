from elo import settings
from django.db import models
from Champions.models import Champion
from elophant.api import api
import requests
import json
import urllib
# Create your models here.

class Summoner(models.Model):
	acctId 			= models.IntegerField(primary_key=True) #use the id from the api as pk so we can have clean queries later
	name 			= models.CharField(max_length=200)
	internalName 	= models.CharField(max_length=200)
	region		 	= models.CharField(max_length=200)
	profileIconId 	= models.IntegerField()
	revisionId 		= models.IntegerField()
	summonerLevel 	= models.IntegerField()
	summonerId 		= models.IntegerField()
	dataVersion 	= models.IntegerField()
	api 			= api(key=settings.ELO_API_KEY)

	#requires self.name and self.region to be set.
	def get(self):
		try:
			data = self.api.summoner_by_name(self.name, self.region) #sets data to the object represented by the json response
			if data is None:
				raise TypeError
		except:
			return False
		
		for k, v in data.iteritems(): #iterate over the response json as key value pairs
			if hasattr(self, k): #check if the object has an attribute with the same name as the key
				setattr(self, k, v) #if it does, set the value of the attribute to the value of key
		self.save() #save the object to the database

	def get_ranked_stats(self):
		try:
			data = self.api.get_ranked_stats(self.acctId, self.region)
			if data is None:
				raise TypeError
		except:
			return False
	
		for each in data:
			try:
				stat = RankedChampionStats.objects.get(ChampionId=each['ChampionId'], summoner=self)
			except:
				stat = RankedChampionStats()
				stat.summoner = self
			for k, v in each.iteritems(): #iterate over the response json as key value pairs
				if k == 'ChampionId':
					setattr(stat, k, Champion.objects.get(pk=v))
				else:
					if hasattr(stat, k): #check if the object has an attribute with the same name as the key
						setattr(stat, k, v) #if it does, set the value of the attribute to the value of key
			stat.save() #save the object


	#http://stackoverflow.com/questions/377454/how-do-i-get-my-python-program-to-sleep-for-50-msec

class RankedChampionStats(models.Model):
	summoner 			= models.ForeignKey(Summoner)
	ChampionId 			= models.ForeignKey(Champion, db_column="ChampionId")
	Wins 				= models.IntegerField()
	Losses 				= models.IntegerField()
	GamesPlayed			= models.IntegerField()
	Kills 				= models.IntegerField()
	Deaths 				= models.IntegerField()
	Assists 			= models.IntegerField()
	DoubleKills			= models.IntegerField()
	TripleKills			= models.IntegerField()
	QuadraKills			= models.IntegerField()
	PentaKills 			= models.IntegerField()
	MaximumKills 		= models.IntegerField()
	MaximumDeaths		= models.IntegerField()
	MinionKills			= models.IntegerField()
	Gold 				= models.IntegerField()
	TurretsDestroyed 	= models.IntegerField()
	DamageDealt 		= models.IntegerField()
	PhysicalDamageDealt	= models.IntegerField()
	MagicalDamageDealt 	= models.IntegerField()
	DamageTaken 		= models.IntegerField()
	TimeSpentDead 		= models.IntegerField()