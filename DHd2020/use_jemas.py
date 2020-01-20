#!/usr/bin/env python

import sys
import os
sys.path.append(os.getcwd()) # for slurm (?)

import pandas as pd
import numpy as np
import spacy
import scipy.stats as st
import utils

import sys
sys.path.append('../')
from jemas4py import jemas

# german emotion lexicon (Schmidke et al., 2014), neutral values are [0., 5., 5.] for VAD
lex = utils.get_lex()
print(lex.head())
print(lex.shape)
neutral = np.array([0.,5.,5.])

# tweets to be analyzed
df = pd.read_csv('tweets.txt', sep = '\t', index_col = 0,encoding="utf-8",dtype=str,engine='python')
tweets = df.text

# analyze tweets using jemas with lex
rt = jemas.batch_process_german(lex, neutral, tweets)
values = [ d['doc_emotion'] for d in rt ] # just the emotion values, not tokens_total or tokens_recognized

print(len(tweets))
print(len(values))

# jemas-predictions into DataFrame
jemas_pred = pd.DataFrame(values, columns = lex.columns)
print(jemas_pred.head())

# adding jemas-predictions to df and saving result
df = df.join(jemas_pred)
print(df.head())

df.to_csv('tweets_emotions_raw.txt', sep = '\t') # before z-transformation

# z-transform values
for emo in jemas_pred.columns:
	print(emo)
	#df[emo] = st.zscore(df[emo], nan_policy = 'omit') # # why nan_policy doesn't work?
	df[emo] = np.around((df[emo] - df[emo].mean())/df[emo].std(), decimals=2)

print(df.head())
df.to_csv('tweets_emotions.txt', sep = '\t') # z-transformed values

