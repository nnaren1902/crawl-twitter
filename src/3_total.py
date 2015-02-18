import config as config
import common as common

d = {}
for hashTag in config.hashtags:
    d[hashTag] = 0;

for hashTag in config.hashtags:
    
    startTime = config.mintime
    endTime = config.maxtime
    timeDelta = 10
    winMinTime = startTime
    
    while(winMinTime+timeDelta <= endTime):
        config.params = config.createParameters(config.API_KEY, hashTag, winMinTime, winMinTime+timeDelta, config.new_only_bool, config.include_metrics_bool, 499)
        
        #Send Request
        request = config.makeRequest(config.url, config.params)
        response = request.getresponse()

        tweets = common.extractTweetsFromResponse(response)
        numberOfTweetsReceived = len(tweets)
        
        if(numberOfTweetsReceived > 498):
            ##reduce the delta size
            timeDelta = timeDelta/2
               
        else:
            d[hashTag] = d[hashTag] + numberOfTweetsReceived
            winMinTime = winMinTime + timeDelta
            timeDelta = 10
            
    ###last time frame
    if(winMinTime != endTime):
        config.params = config.createParameters(config.API_KEY, hashTag, winMinTime,endTime, config.new_only_bool, config.include_metrics_bool, 499)
        
        #Send Request
        request = config.makeRequest(config.url, config.params)
        response = request.getresponse()

        tweets = common.extractTweetsFromResponse(response)
        numberOfTweetsReceived = len(tweets)
        if (numberOfTweetsReceived != 1):
            d[hashTag] = d[hashTag]+numberOfTweetsReceived
                ##only for the end case