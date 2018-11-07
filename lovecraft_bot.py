from twitterbot import TwitterBot
import auth as key
import hmac, base64, hashlib, json
from flask import Flask, request, Response, abort, jsonify, json

app = Flask(__name__)


@app.route('/listener', methods=['GET'])
def validation():
	sha256_hash_digest = hmac.new(key.consumer_secret, msg=request.args.get('crc_token'), digestmod=hashlib.sha256).digest()
	response = {
	'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest)
	}
	return json.dumps(response)

@app.route('/listener', methods=['POST'])
def main():
	requestJson = request.get_json()
	#print(json.dumps(requestJson, indent=4, sort_keys=True))
	if 'tweet_create_events' in requestJson.keys():
		mentioned_name = requestJson['tweet_create_events'][0]['entities'][0]["user_mentions"].get("screen_name")
		if mentioned_name == "Arkham_bot":
			replying_to = requestJson['tweet_create_events'][0]['user']['screen_name']
			tweet_id = requestJson['tweet_create_events'][0]['id_str']
			TwitterBot.reply(replying_to, tweet_id)

	#elif 'follow_events' in requestJson.keys():
		#TwitterBot.follow_back()
	return ('OK')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
