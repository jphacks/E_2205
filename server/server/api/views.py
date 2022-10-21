import os
import datetime
import tweepy
from requests import Response
from requests_oauthlib import OAuth1Session
from django.shortcuts import redirect
from django.http import JsonResponse
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

    if request.method == 'POST':
        access_token = request.POST.get('access_token', '')
        access_token_secret = request.POST.get('access_token_secret', '')

        response = create_client(access_token, access_token_secret).get_home_timeline().json()
        return JsonResponse(response)
    else:
        return JsonResponse({'hello': 'json'})


@csrf_exempt
def page_home(request):
    if request.method == 'POST':
        access_token = request.POST.get('access_token', '')
        access_token_secret = request.POST.get('access_token_secret', '')

        response = create_client(access_token, access_token_secret).get_home_timeline(max_results=100).json()
        next_token = response['meta']['next_token']

        return JsonResponse(response)
    else:
        return JsonResponse({'hello': 'json'})


@csrf_exempt
def create_tweet(request):
    if request.method == 'POST':
        access_token = request.POST.get('access_token', '')
        access_token_secret = request.POST.get('access_token_secret', '')

        new_tweet = request.POST.get('tweet', 'none')
        if (new_tweet != 'none'):
            create_client(access_token, access_token_secret).create_tweet(text=new_tweet)


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
    response_acc = session_acc.post(access_endpoint_url, params={"oauth_verifier": oauth_verifier})
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
