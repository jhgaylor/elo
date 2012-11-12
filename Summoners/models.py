from elo import settings
from django.db import models
from Champions.models import Champion

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

	#requires self.name and self.region to be set.
	def get(self):
		if (self.name == "") or (self.region == ""):
			return False #if either required parameter is unavailable to us we return false
		url = "http://elophant.com/api/v1/"+self.region+"/getSummonerByName?summonerName="+urllib.quote(self.name)+"&key="+settings.ELO_API_KEY
		r = requests.get(url) #send a get request for the response
		data = r.json #sets data to the object represented by the json response
		if data is not None: #make sure we got a response.  The response will be none if they have no data for the request
			for k, v in data.iteritems(): #iterate over the response json as key value pairs
				if hasattr(self, k): #check if the object has an attribute with the same name as the key
					setattr(self, k, v) #if it does, set the value of the attribute to the value of key
			self.save() #save the object

	def get_ranked_stats(self):
		stats = RankedChampionStats()
		stats.summoner = self
		stats.get()


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

	#requires self.summoner to be set.
	def get(self):
		if self.summoner < 1:
			return False #if either required parameter is unavailable to us we return false
		url = "http://elophant.com/api/v1/"+self.summoner.region+"/getRankedStats?accountId="+str(self.summoner.acctId)+"&season=CURRENT&key="+settings.ELO_API_KEY
		r = requests.get(url) #send a get request for the response
		data = r.json #sets data to the object represented by the json response
		if data is not None: #make sure we got a response.  The response will be none if they have no data for the request
			for each in data:
				for k, v in each.iteritems(): #iterate over the response json as key value pairs
					if k == 'ChampionId':
						setattr(self, k, Champion.objects.get(pk=v))
					else:
						if hasattr(self, k): #check if the object has an attribute with the same name as the key
							setattr(self, k, v) #if it does, set the value of the attribute to the value of key
				self.save() #save the object
