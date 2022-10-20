import os
import datetime
from django.http import JsonResponse
from django.shortcuts import redirect
import tweepy
from requests_oauthlib import OAuth1Session

client = tweepy.Client(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)


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

    # print("Access Token       :", access_token)
    # print("Access Token Secret:", access_token_secret)
    # print("User ID            :", acc_token_dict["user_id"])
    # print("Screen Name        :", acc_token_dict["screen_name"])

    client = tweepy.Client(
        os.environ['BEARER_TOKEN'],
        os.environ['CONSUMER_KEY'],
        os.environ['CONSUMER_SECRET'],
        access_token,
        access_token_secret
    )

    tweet_text = f"connected {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    client.create_tweet(text=tweet_text)

    response = redirect('https://twitter.com/home')
    return response


def home_json(request):
    """
    Display Twitter-Timeline.
    """

    if request.method == 'GET':
        response = client.get_home_timeline()
        print(response)
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


def page_home(request):

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

    return JsonResponse({'data': paginator_str})

# @csrf_exempt


def create_tweet(request):
    new_tweet = request.POST.get('tweet', 'none')
    if (new_tweet != 'none'):
        client.create_tweet(text=new_tweet)

    return JsonResponse({'data': new_tweet})
