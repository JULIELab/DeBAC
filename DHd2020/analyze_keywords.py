import utils
import pandas as pd
import numpy as np

tweets = pd.read_csv('tweets_emotions.txt', sep = '\t', index_col = 'tweet_id')
print(tweets.head())
#print(tweets.describe())

keywords = ["Gemeinschaft", "Heimat", "Romantik", "Glauben", "Wesen", "romantisch", "romantisieren"]
parties = tweets.party.unique()

df_valence = pd.DataFrame(columns = parties)
df_counts = pd.DataFrame(columns = parties)

for word in keywords:
	ids = utils.get_ids(word) # tweet_ids containing the word
	tweets_word = tweets.loc[ids] # tweets containing the word
	
	for party in parties:
		tweets_relevant = tweets_word[tweets_word.party == party] # tweets from party containing word
		nr_tweets = len(tweets_relevant)
		if nr_tweets == 0:
			val_mean = 0.
		else:
			val_mean = np.mean(tweets_relevant.valence)
		df_valence.loc[word, party] = np.around(val_mean, decimals=2)
		df_counts.loc[word, party] = int(nr_tweets)

print(df_valence)
df_valence.to_csv('result_valence.txt', sep = '\t')

print(df_counts)
df_counts.to_csv('result_counts.txt', sep = '\t')


