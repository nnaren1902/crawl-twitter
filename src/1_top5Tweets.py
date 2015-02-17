import config as config
import common as common

#########   get response and print out status
request = config.makeRequest(config.url, config.params);
response = request.getresponse()

common.writeResponseAsTweetsToFile(response,[], "../output/top_tweets.txt")
