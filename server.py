import os
# import twitter
from flask import Flask,render_template,send_from_directory
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	import twilio.twiml
	resp = twilio.twiml.Response()
	resp.message('THANKS FOR SIGNING UP, d00d')
	return str(resp)

@app.route('/update')
def chronjob():
	return 'Querying for new food...'	

if __name__ == '__main__':
	# Bind to PORT if defined (environment variable on heroku)
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port, debug=True)


