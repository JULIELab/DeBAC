import tweepy
import os
import pandas as pd
from datetime import datetime, timedelta, timezone

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    return api

# Create API object
api = connect_to_twitter_OAuth()

# fuction to extract data from tweet object
def extract_tweet_attributes(tweet_object):
    # create empty list
    tweet_list =[]
    # loop through tweet objects
    for tweet in tweet_object:
        tweet_id = tweet.id_str # unique integer identifier for tweet
        #text = tweet.text # utf-8 text of tweet
        favorite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        created_at = tweet.created_at # utc time tweet created
        source = tweet.source # utility used to post tweet
        reply_to_status = tweet.in_reply_to_status_id_str # if reply int of orginal tweet id
        reply_to_user_id = tweet.in_reply_to_user_id_str
        reply_to_user_screen_name = tweet.in_reply_to_screen_name # if reply original tweetes screenname
        retweets = tweet.retweet_count # number of times this tweet retweeted
        favorites = tweet.favorite_count # number of time this tweet liked
        lang = tweet.lang
        geo = tweet.geo
        coordinates = tweet.coordinates
        place = tweet.place
        # get full_text
        id_status = api.get_status(tweet_id, tweet_mode="extended")
        RT = False
        try:
          full_text = id_status.retweeted_status.full_text
          RT = True
        except AttributeError:  # Not a Retweet
          full_text = id_status.full_text
        full_text = full_text.replace("\n", " ").replace("\r"," ")
        # append attributes to list
        tweet_list.append({'tweet_id':tweet_id, 
                          'text':full_text, #original:text
                          'if_retweet':RT,
                          'favorite_count':favorite_count,
                          'retweet_count':retweet_count,
                          'created_at':created_at, 
                          'source':source, 
                          'reply_to_status':reply_to_status, 
                          'reply_to_user_id':reply_to_user_id,
                          'reply_to_user_screen_name':reply_to_user_screen_name,
                          'language':lang,
                          'geo':geo,
                          'coordinates':coordinates,
                          'place':place,
                          'get_at':str(datetime.utcnow())})


    #return tweet_list
    
    # create dataframe   
    df = pd.DataFrame(tweet_list, columns=['tweet_id',
                                           'text',
                                           'if_retweet',
                                           'favorite_count',
                                           'retweet_count',
                                           'created_at',
                                           'source',
                                           'reply_to_status',
                                           'reply_to_user_id',
                                           'reply_to_user_screen_name',
                                           'language',
                                           'geo',
                                           'coordinates',
                                           'place',
                                           'get_at'],dtype=str)
    return df

def update_user(user_id):
  user_info = api.get_user(user_id)
  print("Update "+user_id)
  with open("user/"+user_id+".user","w",encoding="utf-8") as f:
    f.write("id: "+user_info.id_str)
    f.write("\n")
    f.write("name: "+user_info.name)
    f.write("\n")
    f.write("screen_name: "+user_info.screen_name)
    f.write("\n")
    f.write("location: "+user_info.location)
    f.write("\n")
    f.write("description: "+user_info.description)
    f.write("\n")
    f.write("followers_count: "+str(user_info.followers_count))
    f.write("\n")
    f.write("friends_count: "+str(user_info.friends_count))
    f.write("\n")
    f.write("created_at: "+str(user_info.created_at))
    f.write("\n")
    f.write("statuses_count: "+str(user_info.statuses_count))

df_MdB = pd.read_csv("MdB_list.tsv",sep="\t",encoding="utf-8",engine='python',dtype=str)

liste = df_MdB['id'].tolist()
print(len(liste))

n = 0
for user_id in liste:
  print("User id: "+user_id)
  user_info = api.get_user(user_id)
  print("User screen name: "+user_info.screen_name)
  update_user(user_id)
  if user_id+".user" not in os.listdir("user"):
    print("create "+user_id)
    with open("user/"+user_id+".user","w",encoding="utf-8") as f:
      f.write("id: "+user_info.id_str)
      f.write("\n")
      f.write("name: "+user_info.name)
      f.write("\n")
      f.write("screen_name: "+user_info.screen_name)
      f.write("\n")
      f.write("location: "+user_info.location)
      f.write("\n")
      f.write("description: "+user_info.description)
      f.write("\n")
      f.write("followers_count: "+str(user_info.followers_count))
      f.write("\n")
      f.write("friends_count: "+str(user_info.friends_count))
      f.write("\n")
      f.write("created_at: "+str(user_info.created_at))
      f.write("\n")
      f.write("statuses_count: "+str(user_info.statuses_count))
    with open("user/"+user_id+".tweet","w",encoding="utf-8") as f:
      f.write("tweet_id")
      f.write("\t")
      f.write("text")
      f.write("\t")
      f.write("if_retweet")
      f.write("\t")
      f.write("favorite_count")
      f.write("\t")
      f.write("retweet_count")
      f.write("\t")
      f.write("created_at")
      f.write("\t")
      f.write("source")
      f.write("\t")
      f.write("reply_to_status")
      f.write("\t")
      f.write("reply_to_user_id")
      f.write("\t")
      f.write("reply_to_user_screen_name")
      f.write("\t")
      f.write("language")
      f.write("\t")
      f.write("geo")
      f.write("\t")
      f.write("coordinates")
      f.write("\t")
      f.write("place")
      f.write("\t")
      f.write("get_at")
      f.write("\n")
    df = pd.read_csv("user/"+user_id+".tweet",sep="\t",engine='python',dtype=str)
  else:
    df = pd.read_csv("user/"+user_id+".tweet",sep="\t",engine='python',dtype=str)
    print(user_id+" alreay exists with "+str(len(df.index))+" tweets.")
  last_second_id = ""
  if len(df.index) > 1:
    last_second_id = df.iloc[1]['tweet_id']
    print("last_second_id: "+last_second_id)
    try:
      df_new = extract_tweet_attributes(api.user_timeline(user_id=user_id,count=200,include_rts=1,since_id=last_second_id))
    except tweepy.error.TweepError:
      pass
  else:
    try:
      df_new = extract_tweet_attributes(api.user_timeline(user_id=user_id,count=200,include_rts=1))
    except tweepy.error.TweepError:
      pass
  df_output = pd.concat([df_new,df])
  df_output.drop_duplicates(subset="tweet_id",keep="last", inplace=True)
  df_output.sort_values(by='created_at', ascending=False, inplace=True)
  if (len(df.index) > 1) and (len(df_output.index) != len(df.index) + len(df_new.index) - 1):
    print("error")
    print("so far",len(df.index))
    print("new",len(df_new.index))
    print("merged",len(df_output.index))
  else:
    print("Correct. "+" "+str(len(df_output.index)-len(df.index))+" are added. Current count: "+str(len(df_output.index)))
  n += len(df_output.index)
  df_output.to_csv("user/"+user_id+".tweet",sep="\t",index=False,header=True,columns=["tweet_id","text","if_retweet","favorite_count","retweet_count","created_at","source","reply_to_status","reply_to_user_id","reply_to_user_screen_name","language","geo","coordinates","place","get_at"])
print(n)
