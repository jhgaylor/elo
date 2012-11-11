from django.db import models
from elo import settings
import requests
import json
# Create your models here.
class Champion(models.Model):
	name = models.CharField(max_length=200)
	id = models.IntegerField(primary_key=True) #use the id from the api as pk so we can have clean queries later

	#this method actually belongs to a manager class, but for now it can stay here.  it doesn't store in the champion itself, but rather gets all champions and stores.
	def get_champions(self):
		url = "http://elophant.com/api/v1/champions?key="+settings.ELO_API_KEY
		r = requests.get(url)
		data = r.json
		for each in data:
			c = Champion()
			for k, v in each.iteritems(): #iterate over the response json as key value pairs
				if hasattr(self, k): #check if the object has an attribute with the same name as the key
					setattr(self, k, v) #if it does, set the value of the attribute to the value of key
			c.save() #save the object
			