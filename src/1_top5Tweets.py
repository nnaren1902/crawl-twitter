import codecs
import json
import random 
import sys

import common as common
import config as config


#hashTag = config.hashtags[random.randrange(0,len(config.hashtags))]
#########   get response and print out status
hashTag = '#SuperBowlXLIX'
config.params = config.createParameters(config.API_KEY, hashTag, config.mintime, config.maxtime, config.new_only_bool, config.include_metrics_bool, 5)
        
#Send Request
request = config.makeRequest(config.url, config.params)
response = request.getresponse()


tweets = common.extractTweetsFromResponse(response)

common.writeResponseAsTweetsToFile(response, tweets,"../output/top_tweets.txt")


for tweet in tweets:
    json_string = json.dumps(tweet,separators=(",",":"),ensure_ascii=False)
    tweetObject = json.loads(json_string,object_hook=common._decode_dict);
        
    
    output = ''
    output += "Tweet's post date: "+str(common.convertTimestampToDate(tweetObject["firstpost_date"]))+"\t\t"
    output += "Text field is:  "+str(tweetObject["tweet"]["text"])+"\t\t"
    output += "The user posting it is :  "+ str(tweetObject["tweet"]["user"]["name"])+"\n"
    print output

