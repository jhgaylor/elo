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

	#SAMPLE_NAMES = ["redrangerftw","Vephoma","Dergonborn","AntiSlash","devilboy945","Dragon1kill","FaceRollR","MasterChieft","Banana111","DerekSucksAtLoL","tc Chimera","davekiller123","LolMe","WangsBeefIsGood","Xbee","tidalbutt","Arcner","syvarious","zark95","KamzX","D O M I N A T 3","thekler","xiaocong","Yendog","Mr Tanks Alot","RufflesRidges","EvilBreed","Lil Venom21","Skipoix","HIghGamingCk","Digital Firewall","Free Champs 0nly","BazookaJay","Funkmaster88","Ryzen Legacy","kwondot","DestroyAllThatsG","RN5xxReckless","VyzVengance","Enevish","Emo Killz","Vakuous","PurpleTabs","KrystalAnn","2 Drunk 2 Aim","Zephrax","Chef The Tony","RaiDiengSaz","CaptainZero0","Clyde Real Ez","Verkato","OREALE","TrueBornSolja","Bowtie Bandito","LOLciferHAHA","cattlepillar","royalstyles","mashpotatoes","LowKey937","haozi","VietDavis","Duy lam12","AllHailTheQueen","Nick1201","Xetene","I Went To Jared","xXicewolfbladeXx","thunderaine","Deblujack13","legendairy251","esceptico","MrGan13","Deadkher","sio00","Biersack","Cowser","killerhurts","EpikS","Bargosa","MystBlanco","dubduce262","aundria","HornyRhino69","Kn3Gr0","Eddy2010","LIPPS","SylvanasWrunner","Mewsers","KsHMetal","Twin Performance","Flowzart","axiommm","Onlyplastic","Baseball Skillz","PokeMyButtPlz","WonJohnWon","Photochronograph","busycoding","MathomaticDimsim","Skyfreak3","Sycip","DiabloHellfire","IonianNirvana","fugle","Lyych","Jseinfeld","Raulstryker","Doi Toshikatsu","Android Four","GR3yZy","jelmod","ikoosh","2od","xTinchix","TacoandBurritos","SteliosV","supermonkeyteam","bato2","ShaCrystal","YMCMBallday","ErrorInSystem","Exzirion","Ianbearpig1337","bctech","stilla","Funybn tic tac","BlastNasy","mistlord","EroSinGoD","GrAViToR99","Schecter28","thekillerofpeopl","snpdng","Joybane","Hafahoodz","DrakoxCR","Rick271","TheOmnipotentZ","BlancaTaza","ADD2012","Epixs","CrowOZ","NeverBackDown2","whatshield","Knightmare Pk","xXAcursedXx","jetpotion","Sw00Sh","BallBagger","Outaylor","Imbapwn","Xcr","deLiTy","LSD and Ecstasy"]

	#requires self.name and self.region to be set.
	def get(self):
		url = "http://elophant.com/api/v1/"+self.region+"/getSummonerByName?summonerName="+urllib.quote(self.name)+"&key="+settings.ELO_API_KEY
		r = requests.get(url)
		data = r.json
		if data is not None:
			self.name=data['name']
			self.internalName = data['internalName']
			self.acctId = data['acctId']
			self.profileIconId = data['profileIconId']
			self.revisionId = data['revisionId']
			self.summonerLevel = data['summonerLevel']
			self.summonerId = data['summonerId']
			self.dataVersion = data['dataVersion']
			self.save()
	#http://stackoverflow.com/questions/377454/how-do-i-get-my-python-program-to-sleep-for-50-msec

class RankedChampionStats(models.Model):
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