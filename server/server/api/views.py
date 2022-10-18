import json
import os
import tweepy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home_json(request):
    """
    Display Twitter-Timeline.
    """
    client = tweepy.Client(
    consumer_key='***',
    consumer_secret='***',
    access_token='***',
    access_token_secret='***'
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