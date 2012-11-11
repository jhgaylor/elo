from Champions.models import Champion
import requests
import json
# Create your views here.
API_KEY = "ormTSJxcEMPj9kJA0p3B"
def get_champions():
	url = "http://elophant.com/api/v1/champions?key="+API_KEY
	r = requests.get(url)
	data = json.loads(r.json)
	print data