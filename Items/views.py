from Items.models import Item
import requests
import json
# Create your views here.
API_KEY = "ormTSJxcEMPj9kJA0p3B"
def get_items():
	url = "http://elophant.com/api/v1/items?key="+API_KEY
	r = requests.get(url)
	data = r.json
	for each in data:
		c = Item()
		c.name=each['name']
		c.epid = each['id']
		c.save()