import pandas as pd

def venues_explore(client,lat,lng, limit,verbose=0):
	'''funtion to get n-places using explore in foursquare, where n is the limit when calling the function.
	This returns a pandas dataframe with name, city ,country, lat, long, address and main category as columns'''
	# create a dataframe
	df_a = pd.DataFrame(columns=['Name', 
	'City', 
	'Latitude',
	'Longitude',
	'Category',
	 'Address'])
	ll=lat+','+lng
	#get venues using client https://github.com/mLewisLogic/foursquare
	venues = client.venues.explore(params={'ll':ll,'limit':limit, 'intent' : 'browse'})
	venues=venues['groups'][0]['items']
	df_venues = pd.DataFrame.from_dict(venues)
	df_venues['venue'][0]
	
	for i, value in df_venues['venue'].items():
		if verbose==1:
			print('i', i, 'name', value['name'], value['location']['city'])
		venueName=value['name']
		venueCity=value['location']['city']
		venueCountry=value['location']['country']
		venueLat=value['location']['lat']
		venueLng=value['location']['lng']
		venueCountry=value['location']['country']
		venueAddress=value['location']['address']
		venueCategory=value['categories'][0]['name']
		df_a=df_a.append([{'Name':venueName, 
						   'City':venueCity,
						   'Country':venueCountry,
						   'Latitude':venueLat,
						   'Longitude':venueLng,
						   'Category':venueCategory,
						   'Address':venueAddress
						  }])
	return df_a.reset_index()