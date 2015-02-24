import datetime
import json
import sys


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
        str1 = json.dumps(tweet,separators=(",",":"),ensure_ascii=False).encode('utf8')
        str1 = str1.replace("&gt;",">")
        str1 = str1.replace("&lt;","<")
        str1 = str1.replace("&amp;","&")
       
        json_string_for_output += str1 + "\n"    
        
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
    
def convertTimestampToDate(unixStartTime):
    dateString = datetime.datetime.fromtimestamp(unixStartTime).strftime('%Y-%m-%d %H:%M:%S')
    return dateString
    
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
        
        
        
def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv
        
    
    