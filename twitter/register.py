from TwitterAPI import TwitterAPI
from os import environ

consumer_key = environ.get('TWITKEY')
consumer_secret = environ.get('TWITSEC')
access_token = environ.get('TWITTOKEN')
access_token_secret = environ.get('TWITTOKENSEC')

ENVNAME = environ.get('ENVNAME')
WEBHOOK_URL = "https://bd7e9730.ngrok.io/listener"

twitterAPI = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

r = twitterAPI.request('account_activity/all/:%s/webhooks' % ENVNAME, {'url': WEBHOOK_URL})

print (r.status_code)
print (r.text)
