import config as config
import common as common
######### change parameters for new request

startTime = config.mintime
endTime = config.maxtime

timeDelta = endTime - startTime
#timeDelta will be divided

offset = timeDelta / 2

window_minTime = startTime
window_maxTime = endTime

#minTime -> minTime + offset
#until minTime + offset == maxTime
#check if offset > maxTime - minTime
    #if yes, make offset = maxTime - minTime 

#########   get response and print out status

# while(offset > 0):    
config.params = config.createParameters(config.API_KEY, config.hashTagToQuery, window_minTime, window_maxTime, config.new_only_bool, config.include_metrics_bool, 500)    
request = config.makeRequest(config.url, config.params)
response = request.getresponse()
tweets = common.extractTweetsFromResponse(response)
print "Number of tweets:" + str(len(tweets))
    