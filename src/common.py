import json
import datetime

def extractTweetsFromResponse(response):
    try:
        print("Extracting tweets from response...")
        response_content = response.read()
        tweet_json_response = json.loads(response_content)
        tweets = tweet_json_response['response']['results']['list']
        return tweets
    except ValueError:
        ##the last time delta may not have any tweets
        print "No tweets for the last delta"
        return [0]

def writeResponseAsTweetsToFile(response,tweets, outputFile,mode='w+'):
    if(len(tweets) == 0):        
        tweets = extractTweetsFromResponse(response)
    print("Writing tweets to file...")    
    if(mode == 'a'):
        output_file = open(outputFile,'a')
    else:
        output_file = open(outputFile,'w+')
    json_string_for_output = ''    
    for tweet in tweets:    
        json_string_for_output += json.dumps(tweet,separators=(",",":")) + "\n"    
        
    output_file.write(json_string_for_output);
    print("Done!")
    output_file.close()
    
def logSearchResults(hashtag, numberOfTweets,unixStartTime,unixEndTime,outputFile,mode):
    startTime = datetime.datetime.fromtimestamp(unixStartTime).strftime('%Y-%m-%d %H:%M:%S')
    endTime = datetime.datetime.fromtimestamp(unixEndTime).strftime('%Y-%m-%d %H:%M:%S')
    
    print("Logging Search Results to file...")    
    if(mode == 'a'):
        output_file = open(outputFile,'a')
    else:
        output_file = open(outputFile,'w+')
    output_string = "Hashtag: "+hashtag+" \tfrom: "+str(startTime)+" \tto: "+str(endTime)+" \tNo. of Results: "+str(numberOfTweets)+"\n"        
    output_file.write(output_string);
    print("Done!")
    output_file.close()
    
    
def logRateResults(hashTag, hashTag_rate, winMinTime,winMaxTime,outputFile):
    startTime = datetime.datetime.fromtimestamp(winMinTime).strftime('%H:%M:%S')
    endTime = datetime.datetime.fromtimestamp(winMaxTime).strftime('%H:%M:%S')
    
    print("Logging popular hashTag rate to file...") 
    
    output_file = open(outputFile,'a')
    output_string = "Hashtag: "+hashTag+" \tfrom: "+str(startTime)+" \tto: "+str(endTime)+" \tHashTag_rate: "+str(hashTag_rate)+"\n"
    output_file.write(output_string)
    print("Done")
    output_file.close()
    
def logCorrelationResults(first_hashTag,hashTag_1_rate,second_hashTag,hashTag_2_rate,samplingTime,outputFile):
    time_sample = datetime.datetime.fromtimestamp(samplingTime).strftime('%H:%M:%S')
    
    print ("logging the data for correlation")
    with open(outputFile,'a') as out_file:
        output_string = "First_popular_hashTag: "+first_hashTag+"\trate: "+str(hashTag_1_rate)+"\tSecond_popular_hashTag: "+second_hashTag+"\trate: "+str(hashTag_2_rate)+"\t"+str(time_sample)+"\n"
        out_file.write(output_string)
        
    
    