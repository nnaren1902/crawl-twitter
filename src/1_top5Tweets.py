import config as config

#########   get response and print out status
request = config.makeRequest();
response = request.getresponse()
# print resp.status, resp.reason

#########   extract tweets
response_content = response.read()
tweet_json_response = config.json.loads(response_content)
tweets = tweet_json_response['response']['results']['list']

# print(json_response);
print(str(tweets))

tweets_file = open('top_tweets.txt','w+')
# 
for tweet in tweets:
    to_write = str(tweet);
    to_write = to_write+"\n";
    tweets_file.write(to_write);    