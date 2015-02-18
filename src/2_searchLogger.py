import config as config
import common as common

######### change parameters for new request


'''
###instead of using the same delta, let's use the maximum possible delta
####this is extremely slow because may requests are made, though this is what they expect
for hashTag in config.hashtags:
    
    startTime = config.mintime
    endTime = config.maxtime
    winMinTime = startTime
    timeDelta = endTime - startTime
    
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
            common.writeResponseAsTweetsToFile(response,tweets, "../output/tweets.txt","a")
            common.logSearchResults(hashTag, numberOfTweetsReceived, winMinTime, winMinTime+timeDelta, "../output/search_log.txt", "a")
            winMinTime = winMinTime + timeDelta
            timeDelta = endTime - winMinTime
'''

d = {}
for hashTag in config.hashtags:
    d[hashTag] = 0;

###for all the hashtags
for hashTag in config.hashtags:
    
    startTime = config.mintime
    endTime = config.maxtime

    timeDelta = endTime - startTime
    lastDelta = timeDelta
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
            lastDelta = timeDelta
            timeDelta = timeDelta/2
               
        else:
            common.writeResponseAsTweetsToFile(response,tweets, "../output/tweets.txt","a")
            common.logSearchResults(hashTag, numberOfTweetsReceived, winMinTime, winMinTime+timeDelta, "../output/search_log.txt", "a")
            #used for part 3
            d[hashTag] = d[hashTag] + numberOfTweetsReceived
            winMinTime = winMinTime + timeDelta
            if (winMinTime + lastDelta <= endTime):
                ##only for the end case
                ###use previous delta, else do don't change timeDelta
                timeDelta = lastDelta
            
    #### for the last piece of time.           
    if winMinTime != endTime:
        config.params = config.createParameters(config.API_KEY, hashTag, winMinTime,endTime, config.new_only_bool, config.include_metrics_bool, 499)
        
        #Send Request
        request = config.makeRequest(config.url, config.params)
        response = request.getresponse()

        tweets = common.extractTweetsFromResponse(response)
        numberOfTweetsReceived = len(tweets)
        if (numberOfTweetsReceived == 1):
            common.logSearchResults(hashTag, 0, winMinTime, endTime, "../output/search_log.txt", "a")
        else:
            common.writeResponseAsTweetsToFile(response,tweets, "../output/tweets.txt","a")
            common.logSearchResults(hashTag, numberOfTweetsReceived, winMinTime, endTime, "../output/search_log.txt", "a")
            d[hashTag] = d[hashTag] + numberOfTweetsReceived   
            
    ##write the counts to a file so that it can be used for part 3
    
    with open('../output/count.txt','a') as count:
        to_write = ''+ hashTag +"\t"+ str(d[hashTag])+"\n"
        count.write(to_write)
        
    
'''
    startTime = config.mintime
    endTime = config.maxtime

    timeDelta = endTime - startTime
    offset = timeDelta / 2

    #########   get response and print out status
    window_minTime = startTime

    while(offset < endTime - window_minTime):     
        window_maxTime = window_minTime + offset   
        config.params = config.createParameters(config.API_KEY, hashTag, window_minTime, window_maxTime, config.new_only_bool, config.include_metrics_bool, 499)    
    
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
            common.writeResponseAsTweetsToFile(response,tweets, "../output/tweets.txt","a")
            common.logSearchResults(hashTag, numberOfTweetsReceived, window_minTime, window_maxTime, "../output/search_log.txt", "a")
            window_minTime = window_maxTime
'''
         
    
