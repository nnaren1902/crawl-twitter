import json

def extractTweetsFromResponse(response):
    print("Extracting tweets from response...")
    response_content = response.read()
    tweet_json_response = json.loads(response_content)
    tweets = tweet_json_response['response']['results']['list']
    return tweets

def writeResponseAsTweetsToFile(response, outputFile):
    print("Writing tweets to file...")
    tweets = extractTweetsFromResponse(response)    
    output_file = open(outputFile,'w+')
    json_string_for_output = ''    
    for tweet in tweets:    
        json_string_for_output += json.dumps(tweet,separators=(",",":")) + "\n"    
        
    output_file.write(json_string_for_output);
    print("Done!")
    