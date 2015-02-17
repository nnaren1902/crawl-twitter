import config as config
import common as common
######### change parameters for new request

startTime = config.mintime
endTime = config.maxtime

timeDelta = endTime - startTime
#timeDelta will be divided

offset = timeDelta / 2

#########   get response and print out status
window_minTime = startTime

while(offset < endTime - window_minTime):     
    window_maxTime = window_minTime + offset   
    config.params = config.createParameters(config.API_KEY, config.hashTagToQuery, window_minTime, window_maxTime, config.new_only_bool, config.include_metrics_bool, 499)    
    
    #Send Request
    request = config.makeRequest(config.url, config.params)
    response = request.getresponse()
    
    tweets = common.extractTweetsFromResponse(response)
    numberOfTweetsReceived = len(tweets)
    if(numberOfTweetsReceived > 498):
        #decrease offsetsize
        timeDelta = window_maxTime - window_minTime
        offset = timeDelta / 2
    else:
#         common.writeResponseAsTweetsToFile(response,tweets, "../output/search_log.txt","a")
        common.logSearchResults(config.hashTagToQuery, numberOfTweetsReceived, window_minTime, window_maxTime, "../output/search_log.txt", "a")
        window_minTime = window_maxTime
             
    