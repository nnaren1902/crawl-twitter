import json
import config as config
import common as common




inputFile = open("../output/tweets.txt");

# request = config.makeRequest(config.url, config.params)
# response = request.getresponse()
# tweets = common.extractTweetsFromResponse(response)

line = inputFile.readline();

tweetObject = json.loads(line,object_hook=common._decode_dict);
# tweetObject = tweets[0]

# for key, value in tweetObject.iteritems() :
#     print key, value

output = ''
output += "Tweet's post date: "+str(common.convertTimestampToDate(tweetObject["firstpost_date"]))+"\n"
output += "Tweet's text content: "+tweetObject["tweet"]["text"]+"\n"
output += "Number of retweets: "+str(tweetObject["tweet"]["retweet_count"])+"\n"
output += "Number of favorites: "+str(tweetObject["tweet"]["favorite_count"])+"\n"
output += "Author's name: "+tweetObject["author"]["name"]+"\n"
output += "Author's nick: "+tweetObject["author"]["nick"]+"\n"
 
print output 
#Or print to file

