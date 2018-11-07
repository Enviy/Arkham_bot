from TwitterAPI import TwitterAPI
from os import environ

consumer_key = environ.get('TWITKEY', None)
consumer_secret = environ.get('TWITSEC', None)
access_token = environ.get('TWITTOKEN', None)
access_token_secret = environ.get('TWITTOKENSEC', None)

envname = environ.get('ENVNAME', None)

twitterAPI = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

r = twitterAPI.request('account_activity/all/:%s/subscriptions' % envname, None, None, "POST")

print(r.status_code)
