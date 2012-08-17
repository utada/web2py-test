# -*- coding: utf-8 -*-

import tweepy

class Twitter:
  consumer = {
    'key': 'NQYFRySHVAv22jlGUwDiJA',
    'secret': 'L2vQUhtEHJBWY2qMDqRyYEcqnNGS7wYoY5duTYvxE'
  }

  def request_token(self):
    auth = tweepy.OAuthHandler(self.consumer["key"],
                               self.consumer["secret"])
    try:
      auth_url = auth.get_authorization_url()
    except tweepy.TweepError, e:
      print e
    request_token = [auth.request_token.key, auth.request_token.secret]
    return [auth_url, request_token]

  def access_token(self, _vars, session):
    verifier = _vars["oauth_verifier"]
    auth = tweepy.OAuthHandler(self.consumer["key"],
                               self.consumer["secret"])
    auth.set_request_token(session.request_token[0], session.request_token[1])

    try:
      access_token = auth.get_access_token(verifier)
    except tweepy.TweepError, e:
      print e
      return False

    return [access_token, auth]

