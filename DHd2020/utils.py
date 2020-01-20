import pandas as pd

# german emotion lexicon (Schmidke et al., 2014)
def get_lex():
    lex = pd.read_excel('ratings.xlsx',encoding="utf-8")

    rename ={'VAL_Mean':'valence',
             'ARO_Mean_(ANEW)':'arousal',
             'DOM_Mean': 'dominance',
             'G-word': 'word'}

    lex.rename(columns=rename, inplace=True)
    for c in lex.columns:
        if c not in rename.values():
            lex.drop(columns=c, inplace=True)

    lex.set_index('word', inplace=True)
    lex = lex[~lex.index.duplicated()]

    return lex

# getting list of IDs for keyword ("Gemeinschaft", "Heimat", "Romantik", "Wesen", "romantisch", "romantisieren")
def get_ids(word):
    path = 'tweets_id/'
    filename = 'id_'+word+'.txt'
    tmp = pd.read_csv(path+filename, sep = '\t', names = ['id'])
    return tmp.id