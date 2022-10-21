from requests_oauthlib import OAuth1Session
import os

API_KEY = consumer_key = os.environ['CONSUMER_KEY']
API_KEY_SECRET = consumer_secret = os.environ['CONSUMER_SECRET']

callback_url = "https://twitter.com/131_develop"
request_endpoint_url = "https://api.twitter.com/oauth/request_token"
authenticate_url = "https://api.twitter.com/oauth/authenticate"

session_req = OAuth1Session(API_KEY, API_KEY_SECRET)
response_req = session_req.post(request_endpoint_url, params={"oauth_callback": callback_url})
response_req_text = response_req.text

oauth_token_kvstr = response_req_text.split("&")
token_dict = {x.split("=")[0]: x.split("=")[1] for x in oauth_token_kvstr}
oauth_token = token_dict["oauth_token"]

print("認証URL:", f"{authenticate_url}?oauth_token={oauth_token}")


oauth_token = input("oauth_token>")
oauth_verifier = input("oauth_Verifier>")

access_endpoint_url = "https://api.twitter.com/oauth/access_token"

API_KEY = consumer_key = os.environ['CONSUMER_KEY']
API_KEY_SECRET = consumer_secret = os.environ['CONSUMER_SECRET']

session_acc = OAuth1Session(API_KEY, API_KEY_SECRET, oauth_token, oauth_verifier)
response_acc = session_acc.post(access_endpoint_url, params={"oauth_verifier": oauth_verifier})
response_acc_text = response_acc.text

access_token_kvstr = response_acc_text.split("&")
acc_token_dict = {x.split("=")[0]: x.split("=")[1] for x in access_token_kvstr}
access_token = acc_token_dict["oauth_token"]
access_token_secret = acc_token_dict["oauth_token_secret"]

print("Access Token       :", access_token)
print("Access Token Secret:", access_token_secret)
print("User ID            :", acc_token_dict["user_id"])
print("Screen Name        :", acc_token_dict["screen_name"])
