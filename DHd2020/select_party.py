import pandas as pd
import numpy as np
import os

tweets = pd.read_csv('tweets_emotions.txt', encoding="utf-8",dtype=str,engine='python', sep = '\t', index_col = 0)

tweets = tweets[['tweet_id', 'text', 'user_id', 'created_at', 'party', 'valence']]

tweets = tweets.sort_values(by=['created_at'])

print(tweets.head().created_at.to_string(index=False))
print(tweets.tail().created_at.to_string(index=False))

# for kw in os.listdir("tweets_id"):
# 	if kw.startswith('id_'):
# 		keyword = kw.split(".")[0][3:]
# 		print(keyword)
# 		liste = []
# 		with open("tweets_id/"+kw,"r",encoding="utf-8") as f:
# 			for ID in f.readlines():
# 				liste.append(ID.strip())
# 		tweets.loc[tweets['tweet_id'].isin(liste)].to_csv(keyword+".tsv",sep="\t",encoding="utf-8")
# 		selected = pd.read_csv(keyword+".tsv", encoding="utf-8",dtype=str,engine='python', sep = '\t', index_col = 0)
# 		selected = selected.sort_values(by=['party', 'tweet_id'])
# 		with open(keyword+".txt","w",encoding="utf-8") as f:
# 			for index, row in selected.iterrows():
# 				f.write(row['text'])
# 				f.write('\n')
# 				f.write(row['valence'])
# 				f.write('\n')
# 				f.write(row['created_at'])
# 				f.write('\n')
# 				f.write(row['party'])
# 				f.write('\n')
# 				f.write(row['user_id'])
# 				f.write('\n')
# 				f.write('http://twitter.com/user/status/'+row['tweet_id'])
# 				f.write('\n\n')
