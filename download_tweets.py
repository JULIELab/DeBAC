#!/usr/bin/env python

import json
import pandas as pd
import time
import tweepy

# load Twitter API credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)

# load tweets-meta.tsv
df = pd.read_csv('tweets-meta.tsv', sep='\t')
df = df[:500] # TODO: so far not possible for whole list (rate limit...), do something about it! sleep?
print(df.head())
IDs = df.tweet_id.tolist() # list of all IDs
print(len(IDs))

############ Tweepy #############

# setting up the API
auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth)

# testing: one tweet
tweet = api.get_status(id="1129249137982099456")
print(tweet.text)  # should return "Seit langem mal wieder eine gute Nachricht ..."

# api.statuses_lookup() is possible for a list of up to 100 ids
# so: splitting IDs into smaller lists (of 100 ids)
ID_chunks = [IDs[x:x+100] for x in range(0, len(IDs), 100)]
print(len(ID_chunks)) # 8871 chunks, each containing (up to) 100 IDs

# creating new DataFrame
df_new = pd.DataFrame(index=IDs, columns=['text'])
df_new.index.name = 'tweet_id'
print(df_new.head())

for chunk in ID_chunks:
    #print(chunk)
    try:
        tweets = api.statuses_lookup(chunk, map_=True)  # map_=True so that tweets no longer available are included
        # print(tweets)
    except tweepy.RateLimitError: # probably not working like this
        print("exceeded rate limit, sleeping for 15 (?) minutes")
        time.sleep(15 * 60)
        continue
    for t in tweets:
        tweet_id = t.id # statuses_lookup seems to change order (?), so just adding a column not possible
        try:
            tweet_text = t.text
        except:
            tweet_text = "None" # if tweet is no longer available
        #print(tweet_id, tweet_text)
        df_new.loc[tweet_id, 'text'] = tweet_text

print(df_new.head())
print(df.shape)

df_new.to_csv('tweets-text.tsv', sep='\t')

"""
for rate limit: maybe something similiar to: https://github.com/seirasto/twitter_download/blob/master/download_tweets_api.py
or: sleep somewhere?
"""
