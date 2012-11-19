from elo import settings
from django.db import models
from Champions.models import Champion
from elophant.api import api
import requests
import json
import urllib
# Create your models here.
class Team(models.Model):
	status 
	tag
	lastGameData
	modifyDate
	teamid #primary key
	lastJoinDate
	secondLastJoinDate

class TeamGameModeStats(models.Model):
	teamid = foreignkey
	teamStatType
	maxRating
	seedRating
	wins
	losses
	rating
	averageGamesPlayed


class TeamRoster(models.Model):
	summoner
	join_date
	invite_date
	status

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
	dodgeStreak		= models.IntegerField(blank=True, default=0)
	previousFirstWinOfDay = models.DateTimeField(null=True)
	runePages 		= models.TextField(blank=True)
	masteryPages	= models.TextField(blank=True)
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

	def get_name(self):
		try:
			data = self.api.get_summoner_names([self.acctId], self.region) #sets data to the object represented by the json response
			if data is None:
				raise TypeError
		except:
			return False
		self.name = data[0]
		self.save() #save the object to the database

	def get_rune_pages(self):
		try:
			data = self.api.get_rune_pages([self.acctId], self.region) #sets data to the object represented by the json response
			if data is None:
				raise TypeError
		except:
			return False
		self.name = data[0]
		self.save() #save the object to the database

	def get_mastery_pages(self):
		try:
			data = self.api.get_mastery_pages(self.acctId, self.region) #sets data to the object represented by the json response
			if data is None:
				raise TypeError
		except:
			return False
		self.name = data[0]
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

	def get_game_mode_stats(self):
		#the call to this will return data to fill GameModeStats records, 
		#but it will also return some data relevant to the summoner in general
		#like last first win of day, dodge streak, leaver penalty
		#will have to store some things on self and some on a record item
		#for now I dont care about the leaver stats or timetrackedstats, so i'll ignore them.
		pass


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

class GameModeStats(models.Model):
	summoner 			= models.ForeignKey(Summoner)
	playerStatSummaryType #key! per summoner, only 1 record per game mode
	modifyDate
	maxRating
	leaves
	losses
	rating
	wins
	#the following are aggregated stats for that game mode
	total_turrets_killed
	total_minion_kills
	#etc... ask api dev for a definitive list?
	#list might be here http://elophant.com/developers/docs/getMostPlayedChampions

class Champion(models.Model):
	id = models.IntegerField(primary_key=True) #use the id from the api as pk so we can have clean queries later
	name = models.CharField(max_length=200)

	#this method actually belongs to a manager class, but for now it can stay here.  it doesn't store in the champion itself, but rather gets all champions and stores.
	def get_champions(self):
		url = "http://elophant.com/api/v1/champions?key="+settings.ELO_API_KEY
		r = requests.get(url)
		data = r.json
		for each in data:
			c = Champion()
			for k, v in each.iteritems(): #iterate over the response json as key value pairs
				if hasattr(c, k): #check if the object has an attribute with the same name as the key
					setattr(c, k, v) #if it does, set the value of the attribute to the value of key
			c.save() #save the object

class Item(models.Model):
	id = models.IntegerField(primary_key=True) #use the id from the api as pk so we can have clean queries later
	name = models.CharField(max_length=200)
	

	#this method actually belongs to a manager class, but for now it can stay here.  it doesn't store in the item itself, but rather gets all items and stores.
	def get_items(self):
		url = "http://elophant.com/api/v1/items?key="+settings.ELO_API_KEY
		r = requests.get(url)
		data = r.json
		for each in data:
			c = Item()
			for k, v in each.iteritems(): #iterate over the response json as key value pairs
				if hasattr(c, k): #check if the object has an attribute with the same name as the key
					setattr(c, k, v) #if it does, set the value of the attribute to the value of key
			c.save() #save the object
			
			