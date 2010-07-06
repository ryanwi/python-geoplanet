# Simple test harness to be run from command-line


from geoplanet import *


geoplanet = GeoPlanet(appid='') #json
#geoplanet = GeoPlanet(appid='', format='xml')

print geoplanet.place(woeid=2507854)
#print geoplanet.continents()
#print geoplanet.countries()['places']['count']
#geoplanet.states.US()
