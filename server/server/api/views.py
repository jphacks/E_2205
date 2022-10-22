import os
import datetime
import tweepy
from requests import Response
from requests_oauthlib import OAuth1Session
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def create_client(access_token: str, access_token_secret: str):
    client = tweepy.Client(
        os.environ['BEARER_TOKEN'],
        os.environ['CONSUMER_KEY'],
        os.environ['CONSUMER_SECRET'],
        access_token,
        access_token_secret,
        return_type=Response
    )

    return client


@csrf_exempt
def home_json(request):
    """
    Display Twitter-Timeline.
    """

    if request.method == 'GET':
        access_token = request.GET['access_token']
        access_token_secret = request.GET['access_token_secret']

        try:
            next_token = request.GET['next_token']
        except KeyError:
            next_token = None

        response = create_client(access_token, access_token_secret).get_home_timeline(
            exclude=['retweets', 'replies'],
            tweet_fields=['created_at', 'author_id', 'public_metrics'],
            expansions=['author_id', 'attachments.media_keys'],
            user_fields=['name', 'username', 'profile_image_url', 'url'],
            media_fields=['url'],
            pagination_token=next_token
        ).json()

        return JsonResponse(response)
    else:
        return HttpResponse('need {access_token,access_token_secret}')


@csrf_exempt
def user_tweets(request):
    """
    Display User Tweets.
    """

    if request.method == 'GET':
        access_token = request.GET['access_token']
        access_token_secret = request.GET['access_token_secret']

        client = create_client(access_token, access_token_secret)
        user_id = client.get_user(username=request.GET['username']).json()['data']['id']

        try:
            next_token = request.GET['next_token']
            response = client.get_users_tweets(id=user_id, pagination_token=next_token).json()
        except KeyError:
            response = client.get_users_tweets(user_id).json()

        return JsonResponse(response)
    else:
        return JsonResponse({'hello': 'json'})

def login(request):
    API_KEY = os.environ['CONSUMER_KEY']
    API_KEY_SECRET = os.environ['CONSUMER_SECRET']

    callback_url = "http://127.0.0.1:8000/oauth/"
    request_endpoint_url = "https://api.twitter.com/oauth/request_token"
    authenticate_url = "https://api.twitter.com/oauth/authenticate"

    session_req = OAuth1Session(API_KEY, API_KEY_SECRET)
    response_req = session_req.post(request_endpoint_url, params={"oauth_callback": callback_url})
    response_req_text = response_req.text

    oauth_token_kvstr = response_req_text.split("&")
    token_dict = {x.split("=")[0]: x.split("=")[1] for x in oauth_token_kvstr}
    oauth_token = token_dict["oauth_token"]

    response = redirect(f'{authenticate_url}?oauth_token={oauth_token}')
    return response


def oauth(request, *args, **kwargs):
    oauth_token = request.GET.get('oauth_token')
    oauth_verifier = request.GET.get('oauth_verifier')

    access_endpoint_url = "https://api.twitter.com/oauth/access_token"

    API_KEY = os.environ['CONSUMER_KEY']
    API_KEY_SECRET = os.environ['CONSUMER_SECRET']

    session_acc = OAuth1Session(API_KEY, API_KEY_SECRET, oauth_token, oauth_verifier)
    response_acc = session_acc.GET(access_endpoint_url, params={"oauth_verifier": oauth_verifier})
    response_acc_text = response_acc.text

    access_token_kvstr = response_acc_text.split("&")
    acc_token_dict = {x.split("=")[0]: x.split("=")[1] for x in access_token_kvstr}
    access_token = acc_token_dict["oauth_token"]
    access_token_secret = acc_token_dict["oauth_token_secret"]

    tweet_text = f"connected {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    create_client(access_token, access_token_secret).create_tweet(text=tweet_text)

    response = {
        "access_token": access_token,
        "access_token_secret": access_token_secret
    }

    return JsonResponse(response)

def twitter_function(type :str, request):

    def rp(name: str): return request.GET[name]

    if request.method == 'GET':
        access_token = request.GET['access_token']
        access_token_secret = request.GET['access_token_secret']

        client = create_client(access_token, access_token_secret)

        if  (type == 'like')        : client.like(rp('tweet_id'))
        elif(type == 'unlike')      : client.unlike(rp('tweet_id'))
        elif(type == 'retweet')     : client.retweet(rp('tweet_id'))
        elif(type == 'unretweet')   : client.unretweet(rp('tweet_id'))
        elif(type == 'create_tweet'): client.create_tweet(text=rp('message'))
        elif(type == 'delete_tweet'): client.delete_tweet(rp('tweet_id'))
        elif(type == 'reply')       : client.create_tweet(in_reply_to_tweet_id=rp('tweet_id'), text=rp('message'))
        elif(type == 'follow')      : client.follow_user(client.get_user(username=rp('username')).json()['data']['id'])
        elif(type == 'unfollow')    : client.unfollow_user(client.get_user(username=rp('username')).json()['data']['id'])

        return JsonResponse({'IsSucceed': 'true'})

@csrf_exempt
def retweet(request):
    return twitter_function('retweet', request)

@csrf_exempt
def unretweet(request):
    return twitter_function('unretweet', request)

@csrf_exempt
def like(request):
    return twitter_function('like', request)

@csrf_exempt
def unlike(request):
    return twitter_function('unlike', request)

@csrf_exempt
def create_tweet(request):
    return twitter_function('create_tweet', request)

@csrf_exempt
def delete_tweet(request):
    return twitter_function('delete_tweet', request)

@csrf_exempt
def reply(request):
    return twitter_function('reply', request)

@csrf_exempt
def follow(request):
    return twitter_function('follow', request)

@csrf_exempt
def unfollow(request):
    return twitter_function('unfollow', request)