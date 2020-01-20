import sys
import pandas as pd
import re
import webbrowser
from pandas import ExcelWriter
#from nltk.tokenize import TweetTokenizer
#tknzr = TweetTokenizer()

user_list_name = input("User list file:")#test.tsv
user_num = 0
tweet_num = 0
token_num = 0
#patterns = ['[Rr]omantik','[Rr]omantisch','[Rr]omantisieren','[Rr]omantierung','[Rr]omantiker','[Bb]laue Blume']
patterns = []
end = False
while not end:
	pattern = input("RegEx to search:")
	if pattern == "":
		end = True
	else:
		patterns.append(pattern)
output_file = input("Output file:")

tweets = []
df_userlist = pd.read_csv(user_list_name,sep="\t",encoding="utf-8",dtype=str,engine='python')
for index, row in df_userlist.iterrows():
	user_num += 1
	df = pd.read_csv("MdB/"+row['id']+".tweet",sep="\t",encoding="utf-8",dtype=str,engine='python')
	for index_u, row_u in df.iterrows():
		tweet_num += 1
		#token_num += len(tknzr.tokenize(row_u['text']))
		for pattern in patterns:
			if re.search(pattern,row_u['text']):
				tweets.append({'id':row_u['tweet_id'],'name':row['username'],'date':row_u['created_at'],'tweet':row_u['text'],'URL':"https://twitter.com/"+row['screenname']+"/status/"+row_u['tweet_id']})

df_result = pd.DataFrame(tweets)
df_result.to_excel(output_file,index=False)
# for t in tweets:
# 	webbrowser.open(t['URL'], 2)
# 	print(t['name'])
# 	print(t['date'])
# 	print(t['tweet'])
# 	print()

# print(user_num)
# print(tweet_num)
# print(token_num)