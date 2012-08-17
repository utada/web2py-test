# -*- coding: utf-8 -*-

from twitter import Twitter
import json

def index():
  # https://twittpane.com:8000/twittpane/default/
  return dict(message="Hello")

def signin():
  session.clear()
  [auth_url, request_token] = Twitter().request_token()
  session.request_token = request_token
  redirect(auth_url)

def oauth_cb():
  [access_token, auth] = Twitter().access_token(request.get_vars, session)
  session.access_token = access_token.key
  session.access_secret = access_token.secret
  
  #if access_token:
  #  session.clear()
  url = 'https://twittpane.com:8000/twittpane/1/twitter'
  redirect(url)

def access_token():
  return json.dumps((session.access_token, session.access_secret))

def twitter():
  #auth.set_access_token(session.access_token, session.access_secret)
  #session.api = tweepy.API(auth)
  return dict(message="Hello")

