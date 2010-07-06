from geoplanet import *


geoplanet = GeoPlanet(appid='.lf0CA3V34GlprmI0No54l93mWlMhLr6TUNN9WK5wFSeY5w2AtnsP2BfBXkjnobgJKUx') #json
#geoplanet = GeoPlanet(appid='.lf0CA3V34GlprmI0No54l93mWlMhLr6TUNN9WK5wFSeY5w2AtnsP2BfBXkjnobgJKUx', format='xml')

print geoplanet.place(woeid=2507854)
#print geoplanet.continents()
#print geoplanet.countries()['places']['count']
#geoplanet.states.US()
