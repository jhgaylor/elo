from Summoners.models import Summoner
import requests
import json
import urllib
# Create your views here.
API_KEY = "ormTSJxcEMPj9kJA0p3B"
def get_summoner(region, name):
	url = "http://elophant.com/api/v1/"+region+"/getSummonerByName?summonerName="+urllib.urlencode(name)+"&key="+API_KEY
	r = requests.get(url)
	data = r.json
	
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
