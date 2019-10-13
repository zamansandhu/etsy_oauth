from django.shortcuts import render
from django.http import HttpResponse
from requests_oauthlib import OAuth1
import requests
import urllib
# Create your views here.
api_key=''
secret_key=''
verification_code=''
oauth_token=''
oauth_token_secret=''

def index(request):
    
    callback_uri='localhost:8000'
    oauth = OAuth1(api_key, client_secret=secret_key,callback_uri=callback_uri)
    request_token_url = r"https://openapi.etsy.com/v2/oauth/request_token?scope=email_r%20listings_r"
    fetch_response = requests.post(url=request_token_url,auth=oauth)#oauth.fetch_request_token(request_token_url)
    print(urllib.parse.unquote(str(fetch_response.content)))
    return HttpResponse('Hello World')
def listing(request):
    oauth = OAuth1(api_key, client_secret=secret_key,resource_owner_key=oauth_token,resource_owner_secret=oauth_token_secret)
    request_token_url = r"https://openapi.etsy.com/v2/listing"
    params = {'oauth_verifier': verification_code}
    fetch_response = requests.post(url=request_token_url,auth=oauth,params=params)#oauth.fetch_request_token(request_token_url)
    print(urllib.parse.unquote(str(fetch_response.content)))
    return HttpResponse('Hello World')


