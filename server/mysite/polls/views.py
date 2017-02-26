from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from twitter_secret import client_key
from twitter_secret import secret_key
from twitter_secret import access_token
from twitter_secret import access_token_secret
from models import Score
import json
import random
import requests
import urllib2
import tweepy

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def score(request, year):
	data = serializers.serialize('json', Score.objects.filter(year=year))
	return HttpResponse(data, content_type='application/json')

def sentiment(request):
  return JsonResponse({'areas': Sentiment().getAreas()})

def tweets(request):
  auth = tweepy.OAuthHandler(client_key, secret_key)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  nw_tweets = api.search(rpp=10, geocode="49.2057,-122.9110,10km")
  tweet = nw_tweets[random.randint(0,9)].text
  url = "http://www.sentiment140.com/api/bulkClassifyJson?appid=bob@apple.com"
  req = urllib2.urlopen(url, json.dumps({'data': [{"text": tweet}]}))
  polarity = json.loads(req.read())['data'][0]['polarity'] # 0, 2, or 4
  sentiment = 'Neutral'
  if int(polarity) == 4:
    sentiment = 'Positive'
  elif int(polarity) == 0:
    sentiment = 'Negative'
  return JsonResponse({'tweet': tweet, 'sentiment': sentiment}, content_type='application/json')

# SAMPLE MOCK DATA GENERATOR JUST FOR DEMO
class Sentiment():
  # Try to get random points across New Westminster
  def getAreas(self):
    return [ \
      {'lat': random.uniform(49.204196, 49.216980), 'lon': random.uniform(-122.930042, -122.907726)}, \
      {'lat': random.uniform(49.200607, 49.208346), 'lon': random.uniform(-122.945663, -122.925922)}, \
      {'lat': random.uniform(49.222250, 49.229201), 'lon': random.uniform(-122.907211, -122.887813)}, \
      {'lat': random.uniform(49.186135, 49.191520), 'lon': random.uniform(-122.952186, -122.934849)}, \
      {'lat': random.uniform(49.225389, 49.233348), 'lon': random.uniform(-122.913391, -122.9)}]
