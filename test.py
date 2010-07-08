# Simple test harness to be run from command-line


from geoplanet import *


geoplanet = GeoPlanet(appid='.lf0CA3V34GlprmI0No54l93mWlMhLr6TUNN9WK5wFSeY5w2AtnsP2BfBXkjnobgJKUx') #json
#geoplanet = GeoPlanet(appid='', format='xml')

#print geoplanet.place.woeid_23424977()
#print geoplanet.continents()
#print geoplanet.countries()['places']['count']


#print geoplanet.place.woeid_2507854.children()

# Get all US states
#print geoplanet.states.US(view='long')
#print geoplanet.place.woeid_23424977.children(filter='type(8);count=51')



# Get counties in a state
#print geoplanet.counties.OR()
#print geoplanet.ADMIN2S.{ADMIN1S}
#print place/[state woeid]/children(filter='type(9)')


#2347596
response = geoplanet.place.woeid_2347563.descendants(filter='type(7);count=1')
print response
print response["places"]["total"]


# Get cities in a county
#print place/[county woeid]/children(filter='type(7)')
