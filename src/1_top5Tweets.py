from config import *

#########   get response and print out status
request = makeRequest();
response = request.getresponse()
# print resp.status, resp.reason

#########   extract tweets
response_content = response.read()
tweet_json_response = json.loads(response_content)
tweets = tweet_json_response['response']['results']['list']

output_file = open('../output/top_tweets.txt','w+')
json_string_for_output = ''
for tweet in tweets:    
    json_string_for_output += json.dumps(tweet,separators=(",",":")) + "\n";    
    
output_file.write(json_string_for_output);
    