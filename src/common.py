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