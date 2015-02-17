import urllib
import httplib
import json
import datetime, time
import random

#########   create UNIX timestamps
start_date = datetime.datetime(2015,02,01,15,0,0)
end_date = datetime.datetime(2015,02,01, 16,0,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'
hashtags = ['#SuperBowlXLIX','#Seahawks','#Patriots','#GoHawks','#GoPatriots','#Halftime','#superbowlcommercials']
new_only_bool = '1'
include_metrics_bool = '1'
tweets_limit = 5

######## Create parameters
def createParameters(apiKey,query,mintime,maxtime,new_only_bool,include_metrics_bool,limit):
    if(limit == -1):
        request_paramters = urllib.urlencode({'apikey' : apiKey, 
                                              'q' :query,
                                              'mintime': str(mintime), 
                                              'maxtime': str(maxtime),
                                              'new_only': new_only_bool, 
                                              'include_metrics':include_metrics_bool})
    else:
        request_paramters = urllib.urlencode({'apikey' : apiKey, 
                                              'q' :query,
                                              'mintime': str(mintime), 
                                              'maxtime': str(maxtime),
                                              'new_only': new_only_bool, 
                                              'include_metrics':include_metrics_bool, 
                                              'limit': limit})
    return request_paramters

#########   create and send HTTP request
def makeRequest(request_url, request_params):
    req_url = request_url + '?' + request_params
    req = httplib.HTTPConnection(host)
    req.putrequest("GET", req_url)
    req.putheader("Host", host)
    req.endheaders()
    req.send('')
    return req

#########   set query parameters
#Choose a random tag from the above list.
hashTagToQuery = hashtags[random.randrange(0,len(hashtags))]
params = createParameters(API_KEY, hashTagToQuery, mintime, maxtime, new_only_bool, include_metrics_bool, tweets_limit)

