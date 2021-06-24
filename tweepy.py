#from textblob import TextBlob
import tweepy
import sys
import pandas as pd
#Each individual will get different keys and tokens so in your case its different
api_key = '%%%%%%%%%%%%%%%%%%%%%%'
api_key_secret ='%%%%%%%%%%%%%%%%%%%%%'
access_token ='###################'
access_token_secret ='##################'
api = tweepy.API(api_key, wait_on_rate_limit=True)

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth_handler)

search_term = ('FarmersBill OR farmersbill2020 OR farmersbill  OR FarmersBill -filter:retweets')
tweet_amount = 1000

tweets=tweepy.Cursor(api.search,q=search_term, lang='en').items(tweet_amount)
#df=pd.DataFrame([tweet.text.replace('RT','') for tweet in tweets],columns=['Tweet'])
df=pd.DataFrame([tweet.text for tweet in tweets],columns=['Tweet'])
#FarmersProtests 

df.to_csv("farmar.csv") #To save the datafreame into csv 
