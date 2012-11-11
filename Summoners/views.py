from Summoners.models import Summoner
import requests
import json
import urllib
# Create your views here.
API_KEY = "ormTSJxcEMPj9kJA0p3B"

SAMPLE_NAMES = ["redrangerftw","Vephoma","Dergonborn","AntiSlash","devilboy945","Dragon1kill","FaceRollR","MasterChieft","Banana111","DerekSucksAtLoL","tc Chimera","davekiller123","LolMe","WangsBeefIsGood","Xbee","tidalbutt","Arcner","syvarious","zark95","KamzX","D O M I N A T 3","thekler","xiaocong","Yendog","Mr Tanks Alot","RufflesRidges","EvilBreed","Lil Venom21","Skipoix","HIghGamingCk","Digital Firewall","Free Champs 0nly","BazookaJay","Funkmaster88","Ryzen Legacy","kwondot","DestroyAllThatsG","RN5xxReckless","VyzVengance","Enevish","Emo Killz","Vakuous","PurpleTabs","KrystalAnn","2 Drunk 2 Aim","Zephrax","Chef The Tony","RaiDiengSaz","CaptainZero0","Clyde Real Ez","Verkato","OREALE","TrueBornSolja","Bowtie Bandito","LOLciferHAHA","cattlepillar","royalstyles","mashpotatoes","LowKey937","haozi","VietDavis","Duy lam12","AllHailTheQueen","Nick1201","Xetene","I Went To Jared","xXicewolfbladeXx","thunderaine","Deblujack13","legendairy251","esceptico","MrGan13","Deadkher","sio00","Biersack","Cowser","killerhurts","EpikS","Bargosa","MystBlanco","dubduce262","aundria","HornyRhino69","Kn3Gr0","Eddy2010","LIPPS","SylvanasWrunner","Mewsers","KsHMetal","Twin Performance","Flowzart","axiommm","Onlyplastic","Baseball Skillz","PokeMyButtPlz","WonJohnWon","Photochronograph","busycoding","MathomaticDimsim","Skyfreak3","Sycip","DiabloHellfire","IonianNirvana","fugle","Lyych","Jseinfeld","Raulstryker","Doi Toshikatsu","Android Four","GR3yZy","jelmod","ikoosh","2od","xTinchix","TacoandBurritos","SteliosV","supermonkeyteam","bato2","ShaCrystal","YMCMBallday","ErrorInSystem","Exzirion","Ianbearpig1337","bctech","stilla","Funybn tic tac","BlastNasy","mistlord","EroSinGoD","GrAViToR99","Schecter28","thekillerofpeopl","snpdng","Joybane","Hafahoodz","DrakoxCR","Rick271","TheOmnipotentZ","BlancaTaza","ADD2012","Epixs","CrowOZ","NeverBackDown2","whatshield","Knightmare Pk","xXAcursedXx","jetpotion","Sw00Sh","BallBagger","Outaylor","Imbapwn","Xcr","deLiTy","LSD and Ecstasy"]

def get_summoner(region, name):
	url = "http://elophant.com/api/v1/"+region+"/getSummonerByName?summonerName="+urllib.quote(name)+"&key="+API_KEY
	r = requests.get(url)
	data = r.json
	if data is not None:
		try:
			c = Summoner.objects.get(acctId=data['acctId'])
		except:
			c = Summoner()

		c.name=data['name']
		c.internalName = data['internalName']
		c.acctId = data['acctId']
		c.profileIconId = data['profileIconId']
		c.revisionId = data['revisionId']
		c.summonerLevel = data['summonerLevel']
		c.summonerId = data['summonerId']
		c.dataVersion = data['dataVersion']
		c.save()
#http://stackoverflow.com/questions/377454/how-do-i-get-my-python-program-to-sleep-for-50-msec
#test