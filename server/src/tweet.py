import os
import tweepy

access_token = input('access_token>')
access_token_secret = input('access_token_secret>')

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    access_token,
    access_token_secret
)

tweet_text = input('text>')

client.create_tweet(text=tweet_text)
