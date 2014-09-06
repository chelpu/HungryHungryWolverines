import os
import twitter
from flask import Flask,render_template,send_from_directory,request
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    return 'We know you\'re a Hungry Hungry Wolverine! Text "signup" to (XXX) XXX - XXXX to nab the latest deets about free food on campus. Powered by Twitter, Twilio, Alchemy and the Ms New Booty under the sea.'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	import twilio.twiml
	resp = twilio.twiml.Response()
	body = request.form.get('Body', 'umich free food')
	api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'), consumer_secret=os.environ.get('CONSUMER_SECRET'), access_token_key=os.environ.get('ACCESS_TOK_KEY'), access_token_secret=os.environ.get('ACCESS_TOK_SECRET'))
	result = api.GetSearch(term=body, result_type="recent", count=1)
	resp.message(result[0].text)
	return str(resp)

@app.route('/update')
def update():
    return 'Querying for new food...'

@app.route('/stop')
def stop():
    return 'Unsubscribed you from our service, so sad to see you go.'

if __name__ == '__main__':
    # Bind to PORT if defined (environment variable on heroku)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)


