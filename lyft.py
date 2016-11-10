import requests
import json
import requests
import logging
import jsontree
from collections import OrderedDict
from collections import namedtuple
#parameters = {"lat": 40.71, "lon": -74}

headers = {"Authorization": "bearer " + "gAAAAABYI7oxKyZdCBlkjg3gR4t43xcJznUP8xbUVWK62xfy22dz777dtAYJPT7bt2QxO4EUkDhaFxDXJA2GZ5WFUudGCFazYIp6WfWwneGH7VHdADMJmHEkDlrRGdcZwAJqateWo9HDUKG0v2st2IgmzxmIkEHbVtP0ytyd6chFmJtgdesM4Ih8Wd_kSjANC00n4bmJGk0LAhnl2Uk1j8k_ve2jPPZZfQ=="}
    #response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
parameters={"start_lat": 37.7772, "start_lng": -122.4233, "end_lat": 37.7972, "end_lng": -122.4533}

sort=True
indents=4

# Make a get request with the parameters.
json_data = requests.get("https://api.lyft.com/v1/cost", params=parameters, headers=headers).json()
min_obj= min(json_data["cost_estimates"],key= lambda ev:ev['estimated_cost_cents_min'])
json_data = json.dumps(min_obj, sort_keys=sort, indent=indents)
		#json_data=json.dumps(jsonArray.json())
		#leng=len(jsonArray.json())
#item_dict = json.loads(json_data)
#json_data=json.dumps(responsedata.json())
#item_dict = json.loads(responsedata)
#print(json_data)
#print(responsedata.content)
print(json_data)
#print(item_dict)
f = open('lyft.txt', 'w')

print >> f,json.dumps(min_obj, sort_keys=sort, indent=indents)
f.close()

#json.dump(data, open('data.txt', 'wb'))
#f = open('out.txt', 'w')


# Print the content of the response (the data the server returned)
#print(response_data)

#print(json_data)
#print(response.headers["content-type"])


#jsonArray = requests.get("https://api.spotcrime.com/crimes.json?lat=%s&lon=%s&radius=%s&key=."%(lat,lon,radius))
		#jsonArray = requests.get("https://api.spotcrime.com/crimes.json?lat=37.334164&lon=-121.884301&radius=0.02&key=.")
		#result=json.dumps
		#someArray = json_decode(jsonArray.json(), true)
#		json_data=json.dumps(jsonArray.json())
#		leng=len(jsonArray.json())
#		item_dict = json.loads(json_data)
