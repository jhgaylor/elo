from Summoners.models import Summoner
from Champions.models import Champion
from Items.models import Item
from time import sleep


#export DJANGO_SETTINGS_MODULE=elo.settings

def populate_items():
	i = Item()
	i.get_items()

def populate_champions():
	c = Champion()
	c.get_champions()


def populate_summoners():
	names = [{'name': "redrangerftw", 'region':'na'},{'name': "Vephoma", 'region':'na'},{'name': "Dergonborn", 'region':'na'},{'name': "AntiSlash", 'region':'na'},{'name': "devilboy945", 'region':'na'},{'name': "Dragon1kill", 'region':'na'},{'name': "FaceRollR", 'region':'na'},{'name': "MasterChieft", 'region':'na'},{'name': "Banana111", 'region':'na'},{'name': "DerekSucksAtLoL", 'region':'na'},{'name': "tc Chimera", 'region':'na'},{'name': "davekiller123", 'region':'na'},{'name': "LolMe", 'region':'na'},{'name': "WangsBeefIsGood", 'region':'na'},{'name': "Xbee", 'region':'na'},{'name': "tidalbutt", 'region':'na'},{'name': "Arcner", 'region':'na'},{'name': "syvarious", 'region':'na'},{'name': "zark95", 'region':'na'},{'name': "KamzX", 'region':'na'},{'name': "D O M I N A T 3", 'region':'na'},{'name': "thekler", 'region':'na'},{'name': "xiaocong", 'region':'na'},{'name': "Yendog", 'region':'na'},{'name': "Mr Tanks Alot", 'region':'na'},{'name': "RufflesRidges", 'region':'na'},{'name': "EvilBreed", 'region':'na'},{'name': "Lil Venom21", 'region':'na'},{'name': "Skipoix", 'region':'na'},{'name': "HIghGamingCk", 'region':'na'},{'name': "Digital Firewall", 'region':'na'},{'name': "Free Champs 0nly", 'region':'na'},{'name': "BazookaJay", 'region':'na'},{'name': "Funkmaster88", 'region':'na'},{'name': "Ryzen Legacy", 'region':'na'},{'name': "kwondot", 'region':'na'},{'name': "DestroyAllThatsG", 'region':'na'},{'name': "RN5xxReckless", 'region':'na'},{'name': "VyzVengance", 'region':'na'},{'name': "Enevish", 'region':'na'},{'name': "Emo Killz", 'region':'na'},{'name': "Vakuous", 'region':'na'},{'name': "PurpleTabs", 'region':'na'},{'name': "KrystalAnn", 'region':'na'},{'name': "2 Drunk 2 Aim", 'region':'na'},{'name': "Zephrax", 'region':'na'},{'name': "Chef The Tony", 'region':'na'},{'name': "RaiDiengSaz", 'region':'na'},{'name': "CaptainZero0", 'region':'na'},{'name': "Clyde Real Ez", 'region':'na'},{'name': "Verkato", 'region':'na'},{'name': "OREALE", 'region':'na'},{'name': "TrueBornSolja", 'region':'na'},{'name': "Bowtie Bandito", 'region':'na'},{'name': "LOLciferHAHA", 'region':'na'},{'name': "cattlepillar", 'region':'na'},{'name': "royalstyles", 'region':'na'},{'name': "mashpotatoes", 'region':'na'},{'name': "LowKey937", 'region':'na'},{'name': "haozi", 'region':'na'},{'name': "VietDavis", 'region':'na'},{'name': "Duy lam12", 'region':'na'},{'name': "AllHailTheQueen", 'region':'na'},{'name': "Nick1201", 'region':'na'},{'name': "Xetene", 'region':'na'},{'name': "I Went To Jared", 'region':'na'},{'name': "xXicewolfbladeXx", 'region':'na'},{'name': "thunderaine", 'region':'na'},{'name': "Deblujack13", 'region':'na'},{'name': "legendairy251", 'region':'na'},{'name': "esceptico", 'region':'na'},{'name': "MrGan13", 'region':'na'},{'name': "Deadkher", 'region':'na'},{'name': "sio00", 'region':'na'},{'name': "Biersack", 'region':'na'},{'name': "Cowser", 'region':'na'},{'name': "killerhurts", 'region':'na'},{'name': "EpikS", 'region':'na'},{'name': "Bargosa", 'region':'na'},{'name': "MystBlanco", 'region':'na'},{'name': "dubduce262", 'region':'na'},{'name': "aundria", 'region':'na'},{'name': "HornyRhino69", 'region':'na'},{'name': "Kn3Gr0", 'region':'na'},{'name': "Eddy2010", 'region':'na'},{'name': "LIPPS", 'region':'na'},{'name': "SylvanasWrunner", 'region':'na'},{'name': "Mewsers", 'region':'na'},{'name': "KsHMetal", 'region':'na'},{'name': "Twin Performance", 'region':'na'},{'name': "Flowzart", 'region':'na'},{'name': "axiommm", 'region':'na'},{'name': "Onlyplastic", 'region':'na'},{'name': "Baseball Skillz", 'region':'na'},{'name': "PokeMyButtPlz", 'region':'na'},{'name': "WonJohnWon", 'region':'na'},{'name': "Photochronograph", 'region':'na'},{'name': "busycoding", 'region':'na'},{'name': "MathomaticDimsim", 'region':'na'},{'name': "Skyfreak3", 'region':'na'},{'name': "Sycip", 'region':'na'},{'name': "DiabloHellfire", 'region':'na'},{'name': "IonianNirvana", 'region':'na'},{'name': "fugle", 'region':'na'},{'name': "Lyych", 'region':'na'},{'name': "Jseinfeld", 'region':'na'},{'name': "Raulstryker", 'region':'na'},{'name': "Doi Toshikatsu", 'region':'na'},{'name': "Android Four", 'region':'na'},{'name': "GR3yZy", 'region':'na'},{'name': "jelmod", 'region':'na'},{'name': "ikoosh", 'region':'na'},{'name': "2od", 'region':'na'},{'name': "xTinchix", 'region':'na'},{'name': "TacoandBurritos", 'region':'na'},{'name': "SteliosV", 'region':'na'},{'name': "supermonkeyteam", 'region':'na'},{'name': "bato2", 'region':'na'},{'name': "ShaCrystal", 'region':'na'},{'name': "YMCMBallday", 'region':'na'},{'name': "ErrorInSystem", 'region':'na'},{'name': "Exzirion", 'region':'na'},{'name': "Ianbearpig1337", 'region':'na'},{'name': "bctech", 'region':'na'},{'name': "stilla", 'region':'na'},{'name': "Funybn tic tac", 'region':'na'},{'name': "BlastNasy", 'region':'na'},{'name': "mistlord", 'region':'na'},{'name': "EroSinGoD", 'region':'na'},{'name': "GrAViToR99", 'region':'na'},{'name': "Schecter28", 'region':'na'},{'name': "thekillerofpeopl", 'region':'na'},{'name': "snpdng", 'region':'na'},{'name': "Joybane", 'region':'na'},{'name': "Hafahoodz", 'region':'na'},{'name': "DrakoxCR", 'region':'na'},{'name': "Rick271", 'region':'na'},{'name': "TheOmnipotentZ", 'region':'na'},{'name': "BlancaTaza", 'region':'na'},{'name': "ADD2012", 'region':'na'},{'name': "Epixs", 'region':'na'},{'name': "CrowOZ", 'region':'na'},{'name': "NeverBackDown2", 'region':'na'},{'name': "whatshield", 'region':'na'},{'name': "Knightmare Pk", 'region':'na'},{'name': "xXAcursedXx", 'region':'na'},{'name': "jetpotion", 'region':'na'},{'name': "Sw00Sh", 'region':'na'},{'name': "BallBagger", 'region':'na'},{'name': "Outaylor", 'region':'na'},{'name': "Imbapwn", 'region':'na'},{'name': "Xcr", 'region':'na'},{'name': "deLiTy", 'region':'na'},{'name': "LSD and Ecstasy", 'region':'na'}]
	
	for n in names:
		s = Summoner()
		s.name = n['name']
		s.region = n['region']
		s.get()
		sleep(1)

def populate_summoners_ranked_stats():
	summoners = Summoner.objects.all()
	for s in summoners:
		s.get_ranked_stats()
		sleep(1)

		
populate_items()
populate_champions()
populate_summoners()
populate_summoners_ranked_stats()