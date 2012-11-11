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
		url = "http://elophant.com/api/v1/"+self.region+"/getSummonerByName?summonerName="+urllib.quote(self.name)+"&key="+settings.ELO_API_KEY
		r = requests.get(url)
		data = r.json
		if data is not None:
			for k, v in data.iteritems():
				if hasAttr(self, k):
					setAttr(self, k, v)

			#self.name=data['name']
			#self.internalName = data['internalName']
			#self.acctId = data['acctId']
			#self.profileIconId = data['profileIconId']
			#self.revisionId = data['revisionId']
			#self.summonerLevel = data['summonerLevel']
			#self.summonerId = data['summonerId']
			#self.dataVersion = data['dataVersion']
			self.save()
	#http://stackoverflow.com/questions/377454/how-do-i-get-my-python-program-to-sleep-for-50-msec

class RankedChampionStats(models.Model):
	summoner 			= models.ForeignKey(Summoner)
	championId 			= models.ForeignKey(Champion)
	wins 				= models.IntegerField()
	losses 				= models.IntegerField()
	gamesPlayed			= models.IntegerField()
	kills 				= models.IntegerField()
	deaths 				= models.IntegerField()
	assists 			= models.IntegerField()
	doubleKills			= models.IntegerField()
	tripleKills			= models.IntegerField()
	quadraKills			= models.IntegerField()
	pentaKills 			= models.IntegerField()
	maximumKills 		= models.IntegerField()
	maximumDeaths		= models.IntegerField()
	minionKills			= models.IntegerField()
	gold 				= models.IntegerField()
	turretsDestroyed 	= models.IntegerField()
	damageDealt 		= models.IntegerField()
	physicalDamageDealt	= models.IntegerField()
	magicalDamageDealt 	= models.IntegerField()
	damageTaken 		= models.IntegerField()
	timeSpentDead 		= models.IntegerField()


# class A():
# 	summoner 			= "summoner"
# 	championId 			= "champ id"