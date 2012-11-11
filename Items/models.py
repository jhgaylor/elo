from django.db import models
from elo import settings
import requests
import json
# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=200)
	epid = models.IntegerField(primary_key=True) #use the id from the api as pk so we can have clean queries later

	#this method actually belongs to a manager class, but for now it can stay here.  it doesn't store in the item itself, but rather gets all items and stores.
	def get_items():
		url = "http://elophant.com/api/v1/items?key="+settings.ELO_API_KEY
		r = requests.get(url)
		data = r.json
		for each in data:
			c = Item()
			c.name=each['name']
			c.epid = each['id']
			c.save()