import config as config
import common as common

total_count = {}
##first part
with open("../output/count.txt") as f:
    for line in f:
        (key, val) = line.split("\t")
        total_count[str(key)] = int(val)
       
       
###for the second plot

popular_hashTag = ['#SuperBowlXLIX']

for hashTag in popular_hashTag:
    
    startTime = config.mintime
    endTime = config.maxtime

    timeDelta = 10
    winMinTime = startTime
     
    while(winMinTime < endTime):
        config.params = config.createParameters(config.API_KEY, hashTag, winMinTime, winMinTime+timeDelta, config.new_only_bool, config.include_metrics_bool, 499)
        
        #Send Request
        request = config.makeRequest(config.url, config.params)
        response = request.getresponse()

        tweets = common.extractTweetsFromResponse(response)
        numberOfTweetsReceived = len(tweets)
        
        hashTag_rate = numberOfTweetsReceived/10
        common.logRateResults(hashTag, hashTag_rate, winMinTime, winMinTime+timeDelta, "../output/rate_log.txt")
        winMinTime = winMinTime + timeDelta
           
       


