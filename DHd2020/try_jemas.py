import sys
sys.path.append('..')
sys.path.append('/home/ruecker/data/dhd2020/')

import pandas as pd
import numpy as np
import spacy
import scipy.stats as st
import utils

from jemas4py import jemas

lex = utils.get_lex()
print(lex.head())
print(lex.describe())
print(lex.shape)
print(lex.loc['Scheitern'])

tweets = ["Der EU-Romantiker Jean Asselborn fordert etwas, das zum Scheitern verurteilt ist. Die osteuropäischen Staaten werden dem niemals zustimmen! https://t.co/Q5Eamb1WAT"]

neutral = np.array([0.,5.,5.])

result = jemas.batch_process_german(lex, neutral, tweets)
print(result)

values = [ d['doc_emotion'] for d in result]
print(values)
