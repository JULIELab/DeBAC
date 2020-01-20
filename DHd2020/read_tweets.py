import pandas as pd
import numpy as np

tweets = pd.read_csv('tweets_emotions.txt', sep = '\t', index_col = 0)

tweets = tweets[['tweet_id', 'text', 'user_id', 'party', 'valence', 'arousal', 'dominance']]
print(tweets.head(10))
print(tweets.shape)
#print(tweets.party.unique())

#print(tweets[tweets.user_id == 14784765]) # example: one specific MdB

#print(tweets[tweets.party == 'Grüne']) # example: one specific party

parties = tweets.party.unique()
for party in parties:
    print(party, "mean VAD values:", np.mean(tweets[tweets.party == party].valence),
                                     np.mean(tweets[tweets.party == party].arousal),
                                     np.mean(tweets[tweets.party == party].dominance))

        
#print(tweets.party.unique()) # corrected type: KINKE > LINKE

#print(tweets.columns)
#print(tweets.dtypes)
