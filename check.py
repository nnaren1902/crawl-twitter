import urllib
import httplib
import json
import datetime, time


#########   create UNIX timestamps
start_date = datetime.datetime(2015,01,14,0,0,0)
end_date = datetime.datetime(2015,01,29, 0,0,0)
mintime = int(time.mktime(start_date.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

API_KEY = '09C43A9B270A470B8EB8F2946A9369F3'
host = 'api.topsy.com'
url = '/v2/content/tweets.json'

#########   set query parameters
params = urllib.urlencode({'apikey' : API_KEY, 'q' :'#SuperBowlXLIX',
                           'mintime': str(mintime), 'maxtime': str(maxtime),
                           'new_only': '1', 'include_metrics':'1', 'limit': 20})



#########   create and send HTTP request
req_url = url + '?' + params
req = httplib.HTTPConnection(host)
req.putrequest("GET", req_url)
req.putheader("Host", host)
req.endheaders()
req.send('')


#########   get response and print out status
resp = req.getresponse()
print resp.status, resp.reason


#########   extract tweets
resp_content = resp.read()
ret = json.loads(resp_content)
tweets = ret['response']['results']['list']

print len(tweets)


j = 0;
for tweet in tweets:
    for i in tweet:
	if i == 'tweet':
	    print i,"	:  	",tweet[i];
	    print "\n";
    j=j+1;
    if j == 5:
	break
