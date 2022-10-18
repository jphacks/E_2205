import json
import os
import tweepy
import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home_json(request):
    """
    Display Twitter-Timeline.
    """
    client = tweepy.Client(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ[ 'CONSUMER_SECRET'],
        access_token=os.environ['ACCESS_TOKEN'],
        access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
    )
    
    if request.method == 'GET':
        response = client.get_home_timeline()
        timeline = []
        for tweets in response:
            string = []
            for tweet in tweets:
                string.append(str(tweet))
            timeline.append(string)

        data = {
            "timeline": timeline
        }
        return JsonResponse(data)

def pageHome(request):
    client = tweepy.Client(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ[ 'CONSUMER_SECRET'],
        access_token=os.environ['ACCESS_TOKEN'],
        access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
    )

    paginator_str = []
    for users_tweets in tweepy.Paginator(
        client.get_home_timeline,
        exclude=['retweets', 'replies'],
        tweet_fields=['public_metrics'],
        max_results=100,
        start_time=datetime.datetime.now() - datetime.timedelta(days=1)
    ):
        tweets_str = []
        for tweet in users_tweets.data:
            tweets_str.append(str(tweet.data)) 
    
        paginator_str.append(tweets_str)

    return JsonResponse({ 'data' : paginator_str })