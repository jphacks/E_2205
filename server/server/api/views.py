import os
import datetime
import tweepy
from requests import Response
from requests_oauthlib import OAuth1Session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class IndexView(View):

    def get(self, request, *args, **kwargs):
        if not 'user_id' in request.session:
            return redirect('/login/')

        access_token = request.session['access_token']
        access_token_secret = request.session['access_token_secret']

        client = tweepy.Client(
            os.environ['BEARER_TOKEN'],
            os.environ['CONSUMER_KEY'],
            os.environ['CONSUMER_SECRET'],
            access_token,
            access_token_secret,
            return_type=Response
        )

        contents = {
            "access_token": access_token,
            "access_token_secret": access_token_secret,
            "user_id": request.session['user_id'],
            "screen_name": request.session['screen_name'],
            "home": client.get_home_timeline().json()
        }
        return render(request, "api/index.html", contents)

    def post(self, request, *args, **kwargs):
        if not 'user_id' in request.session:
            return redirect('/login/')

        tweet = request.POST["tweet"]
        access_token = request.session['access_token']
        access_token_secret = request.session['access_token_secret']

        client = tweepy.Client(
            os.environ['BEARER_TOKEN'],
            os.environ['CONSUMER_KEY'],
            os.environ['CONSUMER_SECRET'],
            access_token,
            access_token_secret
        )

        if (tweet != None):
            client.create_tweet(text=tweet)

        return redirect('/')


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


def oauth(request):
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

    request.session['access_token'] = acc_token_dict["oauth_token"]
    request.session['access_token_secret'] = acc_token_dict["oauth_token_secret"]
    request.session['user_id'] = acc_token_dict["user_id"]
    request.session['screen_name'] = acc_token_dict["screen_name"]

    response = redirect('/')
    return response


def logout(request):
    request.session.clear()
    return HttpResponse('logout')
