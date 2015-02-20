import config as config
import common as common

first_popular = '#SuperBowlXLIX'
second_popular = '#Seahawks'

startTime = config.mintime
endTime = config.maxtime

timeDelta = 10
winMinTime = startTime
     
while(winMinTime < endTime):
    #Send Request for first popular hashtag
    config.params = config.createParameters(config.API_KEY, first_popular, winMinTime, winMinTime+timeDelta, config.new_only_bool, config.include_metrics_bool, 499)
    request = config.makeRequest(config.url, config.params)
    response = request.getresponse()

    tweets_1 = common.extractTweetsFromResponse(response)
    numberOfTweetsReceived_1 = len(tweets_1)
        
    hashTag_1_rate = numberOfTweetsReceived_1/10

    #Send Request for second popular hashtag
    config.params = config.createParameters(config.API_KEY, second_popular, winMinTime, winMinTime+timeDelta, config.new_only_bool, config.include_metrics_bool, 499)
    request = config.makeRequest(config.url, config.params)
    response = request.getresponse()

    tweets_2 = common.extractTweetsFromResponse(response)
    numberOfTweetsReceived_2 = len(tweets_2)
        
    hashTag_2_rate = numberOfTweetsReceived_2/10
    
    ##log the results
    common.logCorrelationResults(first_popular, hashTag_1_rate, second_popular,hashTag_2_rate, winMinTime+timeDelta, "../output/correlation_log.txt")
    
    ##increment the window
    winMinTime = winMinTime + timeDelta
    
    