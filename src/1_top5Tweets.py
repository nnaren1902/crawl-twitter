import config as config
import common as common
import random 
import json

#hashTag = config.hashtags[random.randrange(0,len(config.hashtags))]
#########   get response and print out status
hashTag = '#SuperBowlXLIX'
config.params = config.createParameters(config.API_KEY, hashTag, config.mintime, config.maxtime, config.new_only_bool, config.include_metrics_bool, 5)
        
#Send Request
request = config.makeRequest(config.url, config.params)
response = request.getresponse()

tweets = common.extractTweetsFromResponse(response)
'''
for tweet in tweets:
    json_string = json.dumps(tweet,separators=(",",":"))
    tweetObject = json.loads(json_string);
        
    
    output = ''
    output += "Tweet's post date: "+str(common.convertTimestampToDate(tweetObject["firstpost_date"]))+"\t\t"
    output += "Text field is:  "+str(tweetObject["tweet"]["text"]).encode("utf8")+"\t\t"
    output += "The user posting it is :  "+ str(tweetObject["tweet"]["user"]["name"]).encode("utf8")+"\n"
    print output
 '''       
common.writeResponseAsTweetsToFile(response, tweets,"../output/top_tweets.txt")


