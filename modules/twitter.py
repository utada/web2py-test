# -*- coding: utf-8 -*-

import tweepy

class Twitter:
  consumer = {
    'key': 'NQYFRySHVAv22jlGUwDiJA',
    'secret': 'L2vQUhtEHJBWY2qMDqRyYEcqnNGS7wYoY5duTYvxE'
  }

  def oauth(self):
    auth = tweepy.OAuthHandler(self.consumer["key"],
                               self.consumer["secret"])
    try:
      auth_url = auth.get_authorization_url()
    except tweepy.TweepError, e:
      print e
    session.set('request_token', (auth.request_token.key, auth.request_token.secret)
    request_token.put()
    redirect(auth_url)

  def oauth_cb(self):
    verifier = request.GET.get('oauth_verifier')
    auth = tweepy.OAuthHandler(self.consumer["key"],
                               self.consumer["secret"])
    token = session.get('request_token')
    session.delete('request_token')
    auth.set_request_token(token[0], token[1])

    try:
      auth.get_access_token(verifier)
    except tweepy.TweepErroor, e:
      print e

    self.api = tweepy.API(auth)


