# -*- coding: utf-8 -*-

import tweepy
from tweepy.parsers import JSONParser
import json
import cPickle as pickle

consumer = {
  'key': 'NQYFRySHVAv22jlGUwDiJA',
  'secret': 'L2vQUhtEHJBWY2qMDqRyYEcqnNGS7wYoY5duTYvxE'
}

def index():
  return 'test'

def verify_credentials():
  auth = tweepy.OAuthHandler(consumer["key"],
                             consumer["secret"])
  auth.set_access_token(session.access_token, session.access_secret)
  api = tweepy.API(auth_handler=auth, parser=JSONParser())
  j = api.verify_credentials()
  json_str = json.dumps(j, encoding="utf-8")

  response.cookies['screen_name'] = j["screen_name"]
  response.cookies['screen_name']['path'] = '/'
  response.cookies['profile_image_url'] = j["profile_image_url"]
  response.cookies['profile_image_url']['path'] = '/'
  response.cookies['id_str'] = j["id_str"]
  response.cookies['id_str']['path'] = '/'

  return str(json_str)

def saved_searches():
  auth = tweepy.OAuthHandler(consumer["key"],
                             consumer["secret"])
  auth.set_access_token(session.access_token, session.access_secret)
  api = tweepy.API(auth_handler=auth, parser=JSONParser())
  j = api.saved_searches()
  json_str = json.dumps(j, encoding="utf-8")

  #response.cookies['saved_searches'] = json_str;
  #response.cookies['saved_searches']['path'] = '/'
  return str(json_str)

def home_timeline():
  # https://twittpane.com:8000/twittpane/api/home_timeline
  since_id = 0
  count = 20
  auth = tweepy.OAuthHandler(consumer["key"],
                             consumer["secret"])
  auth.set_access_token(session.access_token, session.access_secret)
  api = tweepy.API(auth_handler=auth, parser=JSONParser())
  json = api.home_timeline(count=count)
  return str(json)


