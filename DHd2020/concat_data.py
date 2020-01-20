import pandas as pd
import os

df = pd.DataFrame(columns = ['tweet_id', 'text', 'if_retweet', 'favorite_count', 'retweet_count',
							 'created_at', 'source', 'reply_to_status', 'reply_to_user_id', 'reply_to_user_screen_name',
							 'language', 'geo', 'coordinates', 'place', 'get_at', 'user_id', 'party'])


party_list = pd.read_csv('MdB_list.tsv',sep ='\t',index_col=0,encoding="utf-8",engine='python')
print(party_list.head())

path_tweets = 'MdB/'
dirs = os.listdir(path_tweets)

counter = 0
for file in dirs:
	if file.endswith('.tweet'):
		user_id = file.split('.')[0]
		print(counter)
		print(file)
		print(user_id)
		party = party_list.loc[int(user_id), 'party']
		print(party)
		tmp = pd.read_csv(path_tweets+file, sep = '\t',encoding="utf-8",dtype=str,engine='python')
		tmp['user_id'] = user_id
		tmp['party'] = party
		counter +=1

		df = df.append(tmp, ignore_index=True)

print(df.head())
print(df.tail())
print(df.shape)

path_target = ''
df.to_csv(path_target+'tweets.txt', sep = '\t')

