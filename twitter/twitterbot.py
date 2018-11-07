import tweepy, time, json
import auth as key
from sample import sample
from sample import main as get_args

#args = get_args()
#sample_output = sample(args)

class TwitterBot:
	def __init__(self, listen, reply):
		auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
		auth.set_access_token(key.access_token, key.access_token_secret)
		self.api = tweepy.API(auth)

	"""def validation():
		sha256_hash_digest = hmac.new(key.consumer_secret, msg=request.args.get('crc_token'), digestmod=hashlib.sha256).digest()
		response = {
	    'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest)
		}
		return json.dumps(response)"""

	def reply(self, replying_to, tweet_id):
    	reply_prefix = '@%s ' % (replying_to)
    	reply_text = reply_prefix + sample_output
		self.api.update_status(status=reply_text, in_reply_to_status_id=tweet_id)

	#def reply_to_mention(self):
		#for mention in self.api.mentions_timeline():
			#if any(t in mention.text.lower() for t in self.listen) and mention.id not in self.replies:
				#try:
					#self.tweet(self.reply.format(mention.user.screen_name), mention.id)
					#self.api.create_favorite(mention.id)
					#time.sleep(5)
				#except tweepy.TweepError:
					#pass
