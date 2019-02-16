# Foursquare api tools (foursquare\_api\_tools)
Some functions to interact with foursquare using 'foursquare' package

## Small intro

I needed to get the venues around a coordinate for a project, but wanted to get them on a dataframe to play with the data using pandas.

I found [https://pypi.python.org/pypi/foursquare/]() which works really good, but still had to clean the result, this this.

I've only tried this with [https://developer.foursquare.com/docs/api/configuration/authentication](Userless Auth from Foursquare). AS I'm using _foursquare_ package it should work with user authentication.


## Installation

```python 
pip install foursquare

pip install git+https://github.com/dacog/foursquare_api_tools.git#egg=foursquare_api_tools
```
If you are using Jupyter Notebooks use:

```python
!pip install foursquare

!pip install git+https://github.com/dacog/foursquare_api_tools.git#egg=foursquare_api_tools
```

## Example of use

### Import libraries

```python
from foursquare_api_tools import foursquare_api_tools as ft
````

### Initialize the client
```python
CLIENT_ID = 'YOUR_CLIENT_ID' # your Foursquare ID
CLIENT_SECRET = 'YOUR_SECRET' # your Foursquare Secret
VERSION = '20180605' # Foursquare API version`
```
this example is **Userless Auth**

```python 
# Construct the client object 
client = fs.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, version=VERSION)
```

### Use the function
```python
venues_explore(client,lat='40.7233',lng='-74.0030',limit=100)
```

## Example

Here is an example on dataplatform.cloud.ibm.com
[https://gist.github.com/e26e21df3b93860e75fc374be89a1a53]()


![Example image](https://github.com/dacog/foursquare_api_tools/blob/master/example.png?raw=true)

## More details about usage
```python
def venues_explore(client,lat,lng, limit=100, verbose=0, sort='popular', radius=2000, offset=1, day='any'):
	'''funtion to get n-places using explore in foursquare, where n is the limit when calling the function.
	This returns a pandas dataframe with name, city ,country, lat, long, address and main category as columns
	Arguments: *client, *lat, *long, limit (defaults to 100), radius (defaults to 2000), verbose (defaults to 0), offset (defaults to 1), day (defaults to any)'''

```
