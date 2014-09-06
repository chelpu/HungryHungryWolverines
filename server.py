import os
import twitter
from flask import Flask,render_template,send_from_directory,request
import sqlalchemy

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	import twilio.twiml
	resp = twilio.twiml.Response()
	# body = request.args.get('Body', 'umich free food')
	body = request.form['Body']
	print body
	api = twitter.Api(consumer_key='', consumer_secret='', access_token_key='', access_token_secret='')
	result = api.GetSearch(term=body, result_type="recent", count=1)
	resp.message(result[0].text)
	return str(resp)

@app.route('/chronjob')
def chronjob():
	return 'CHRONJOB'	

if __name__ == '__main__':
	# Bind to PORT if defined (environment variable on heroku)
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port, debug=True)


