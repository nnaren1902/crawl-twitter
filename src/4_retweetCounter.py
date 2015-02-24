# For every unique tweet in your data, find how many retweets it has. Plot the number of tweets
# retweeted times, over number of retweets , i.e. for each value of , show how many tweets exist 
# that have retweets. Draw this plot in linear scales once, and another time in log-log scale. 
# Can you fit a line to any of these plots?

import json
import config as config
import common as common
import os

inputFile = open("../output/tweets.txt");
line = inputFile.readline();

tweetsIndexedByRetweetCount = {}; #Not indexed per se, but the keys of the dictionary represent the count.
tweetsCountIndexedByRetweetCount = {}

with open('../output/tweets.txt') as inputFileObject:
    for line in inputFile:
        tweetObject = json.loads(line);        
        if (tweetObject != 0) and (type(tweetObject) is dict) :
#             numberOfRetweetsForCurrentTweet = tweetObject["tweet"]["retweet_count"]
            numberOfRetweetsForCurrentTweet = tweetObject["metrics"]["citations"]["total"]            
            if not(tweetsIndexedByRetweetCount.has_key(numberOfRetweetsForCurrentTweet)):                        
                tweetsIndexedByRetweetCount[numberOfRetweetsForCurrentTweet] = [];
                tweetsCountIndexedByRetweetCount[numberOfRetweetsForCurrentTweet] = 0;            
            tweetsIndexedByRetweetCount[numberOfRetweetsForCurrentTweet].append(tweetObject);
            tweetsCountIndexedByRetweetCount[numberOfRetweetsForCurrentTweet] = tweetsCountIndexedByRetweetCount[numberOfRetweetsForCurrentTweet] + 1;
            
            print "Tweet count for "+str(numberOfRetweetsForCurrentTweet)+ " retweets: "+ str(tweetsCountIndexedByRetweetCount[numberOfRetweetsForCurrentTweet])
        
output_file = open("../output/retweetCounter.txt",'w')
stringForOutput = "Retweet Count\t:\tNumber of Tweets\n"
countArrayForRetweets = []
max = 0;
for key, value in tweetsCountIndexedByRetweetCount.iteritems() :
    stringForOutput += "\t"+str(key)+"\t:\t"+str(value)+"\n"
    print stringForOutput        
    countArrayForRetweets.append(key)
    if(key>max):
        max = key
    
output_file.write(stringForOutput);    
output_file.close();
 
sortedRetweetArrayWithIntervals = [0] * (max+1)

for key, value in tweetsCountIndexedByRetweetCount.iteritems() :
    sortedRetweetArrayWithIntervals[key] = value;

for i in range(0,len(sortedRetweetArrayWithIntervals)):
    stringForOutput += "\t"+str(i)+"\t:\t"+str(sortedRetweetArrayWithIntervals[i])+"\n"
    
print stringForOutput





# output = ''
#         output += "Tweet's post date: "+str(common.convertTimestampToDate(tweetObject["firstpost_date"]))+"\n"
#         output += "Tweet's text content: "+tweetObject["tweet"]["text"]+"\n"
#         output += "Number of retweets: "+str(tweetObject["tweet"]["retweet_count"])+"\n"
#         output += "Number of favorites: "+str(tweetObject["tweet"]["favorite_count"])+"\n"
#         output += "Author's name: "+tweetObject["author"]["name"]+"\n"
#         output += "Author's nick: "+tweetObject["author"]["nick"]+"\n"
