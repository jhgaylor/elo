from Summoners.models import Summoner
import requests
import json
# Create your views here.
API_KEY = "ormTSJxcEMPj9kJA0p3B"
def get_summoner(region, name):
	url = "http://elophant.com/api/v1/"+region+"/getSummonerByName?summonerName="+name+"&key="+API_KEY
	r = requests.get(url)
	data = r.json
	for each in data:
		c = Summoner()

		c.name=each['name']
		c.internalName = each['internalName']
		c.acctId = each['acctId']
		c.profileIconId = each['profileIconId']
		c.revisionId = each['revisionId']
		c.summonerLevel = each['summonerLevel']
		c.summonerId = each['summonerId']
		c.dataVersion = each['dataVersion']
		c.save()
