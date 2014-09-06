import os
import twitter
from flask import Flask,render_template,send_from_directory
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	import twilio.twiml
	resp = twilio.twiml.Response()
	resp.message('THANKS FOR SIGNING UP, d00d')
	return str(resp)

@app.route('/chronjob')
def chronjob():
	return 'CHRONJOB'	

# this guy handles static files
@app.route('/<path:filename>')
def send_pic(filename):
	print(filename)
	return send_from_directory('./public/', filename)

if __name__ == '__main__':
	# Bind to PORT if defined (environment variable on heroku)
	port = int(os.environ.get('PORT', 5000))
	app.run(host='127.0.0.1', port=port, debug=True)


