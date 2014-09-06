import os
import twitter
from flask import Flask,render_template,send_from_directory
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route('/signup')
def signup():
	return 'SIGNUP'

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
	port = int(os.environ.get('PORT', 3000))
	app.run(host='0.0.0.0', port=port, debug=True)


