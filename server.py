import os
import tweepy
from flask import Flask,render_template,send_from_directory,request

app = Flask(__name__)

subscribers = {}
twilio_number = '+17348905282'
cur_tweet = {'0':''}

@app.route('/', methods=['GET', 'POST'])
def main():
    return 'We know you\'re a Hungry Hungry Wolverine! Text "signup" to (XXX) XXX - XXXX to nab the latest deets about free food on campus. Powered by Twitter, Twilio, Alchemy and the Ms New Booty under the sea.'


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    import twilio.twiml
    resp = twilio.twiml.Response()
    number = request.form.get('From', '')
    if number not in subscribers:
    	subscribers[number] = {}
    body = request.form.get('Body', 'umich free food')
    if body.lower() == 'stop' and number in subscribers:
    	del subscribers[number]
    	resp.message('You\'ve successfully unsubscribed! Bye bye.')
    	return str()
    return str(resp)


@app.route('/update')
def update():
    from twilio.rest import TwilioRestClient

    auth = tweepy.OAuthHandler(consumer_key=os.environ.get('CONSUMER_KEY'), consumer_secret=os.environ.get('CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('ACCESS_TOK_KEY'), os.environ.get('ACCESS_TOK_SECRET'))

    api = tweepy.API(auth)

    query = 'umich free food'
    count = 1
    result = [status for status in tweepy.Cursor(api.search, q=query, geocode="42.2814, 83.7483, 5mi", result_type='recent').items(count)]

    if result[0].text != cur_tweet['0']:
    	cur_tweet['0'] = result[0].text
    else:
        return ''

    client = TwilioRestClient(account=os.environ.get('TWILIO_SID'), token=os.environ.get('TWILIO_SECRET'))
    for number in subscribers:
        client.sms.messages.create(body=cur_tweet['0'], to=number, from_=twilio_number)
    return 'Querying for new food...'

@app.route('/stop')
def stop():

    return 'Unsubscribed you from our service, so sad to see you go.'

if __name__ == '__main__':
    # Bind to PORT if defined (environment variable on heroku)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)


