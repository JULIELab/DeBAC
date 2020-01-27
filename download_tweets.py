#!/usr/bin/env python

import json
import pandas as pd
import tweepy
import time

# load Twitter API credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# load tweets-meta.tsv
df = pd.read_csv('tweets-meta.tsv', sep='\t')
print(df.head())
print(df.shape)

############ Tweepy #############

# setting up the API
auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# testing: one tweet
#tweet = api.get_status(id="1129249137982099456", map_=True, tweet_mode='extended')
#print(tweet.full_text)  # should return "Seit langem mal wieder eine gute Nachricht ..."

# reading in the empty or partly filled file or creating it if it doesn't exist
try:
    tmp = pd.read_csv('tweets-text_partly.tsv', sep='\t', index_col=0)
    tmp.index.name = 'tweet_id'
    print("reading in the partly filled file")
except:
    print("creating initial file")
    tmp = pd.DataFrame(index=df.tweet_id.tolist(), columns=['text'])
    tmp.index.name = 'tweet_id'
    tmp.to_csv('tweets-text_partly.tsv', sep='\t')
print(tmp.head())
print(tmp.shape)

# looking for the still "empty" IDs
IDs = tmp[tmp.text.isnull()].index.tolist()
print("remaining number of IDs to be looked up:", len(IDs))

while len(IDs) > 0:
    # api.statuses_lookup() is possible for a list of up to 100 IDs
    # so: splitting IDs into smaller lists (of 100 IDs)
    ID_chunks = [IDs[x:x+100] for x in range(0, len(IDs), 100)]
    #print(len(ID_chunks))

    for chunk in ID_chunks:
        #print(chunk)
        try:
            tweets = api.statuses_lookup(chunk, map_=True, tweet_mode='extended')  # map_=True so that tweets no longer available are included
                                                                                   # tweet_mode='extended' so that long tweets are not truncated
        except: # if sth. goes wrong, e.g. if twitter is not responding
            time.sleep(30)
            continue # goes to next chunk (not problematic because missing IDs will be noticed later)
        for t in tweets:
            tweet_id = t.id
            #print(tweet_id)
            if hasattr(t, "retweeted_status"): # check if tweet is a retweet
                tweet_text = t.retweeted_status.full_text # take original tweet's full text
            elif hasattr(t, "full_text"): # normal tweet (still available)
                tweet_text = t.full_text
            else:
                tweet_text = "None" # if tweet is no longer available
            tweet_text = tweet_text.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ') # replace whitespaces with spaces
            tmp.loc[tweet_id, 'text'] = tweet_text
        #print("saving...") #TODO: saving this often maybe not necessary and too time consuming?
        tmp.to_csv('tweets-text_partly.tsv', sep='\t') # overwriting partly filled file

    # reading in the partly filled file
    tmp = pd.read_csv('tweets-text_partly.tsv', sep='\t', index_col=0)
    # looking for the still "empty" IDs
    IDs = tmp[tmp.text.isnull()].index.tolist()

# renaming the final file
df_full = pd.read_csv('tweets-text_partly.tsv', sep='\t', index_col=0)
df_full.to_csv('tweets-text.tsv', sep='\t')
print("done downloading all tweets")


