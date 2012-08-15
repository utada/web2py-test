# -*- coding: utf-8 -*-

from twitter import Twitter

def index():
  # https://twittpane.com:8000/twittpane/default/
  return dict(message="Hello")

def signin():
  url = Twitter().getToken()
  redirect(url)

def verify():
  return 'verify'

