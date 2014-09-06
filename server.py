import os
from flask import Flask,render_template,send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
import pyjade

app = Flask(__name__)
# use the jade template engine
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')


@app.route('/')
def index():
	obj = {
		"title": "Hungry Hungry Wolverines",
	};
	return render_template('index.jade', **obj)

@app.route('/signup/')
def signup():
	obj = {
		"text": "You found the signup page"
	};
	return render_template('index.jade', **obj)	

@app.route('/chronjob/')
def chronjob():
	obj = {
		"text": "Go away, you don't belong here"
	};
	return render_template('index.jade', **obj)		

# this guy handles static files
@app.route('/<path:filename>')
def send_pic(filename):
	print(filename)
	return send_from_directory('./public/', filename)

if __name__ == '__main__':
	# Bind to PORT if defined (environment variable on heroku)
	port = int(os.environ.get('PORT', 3000))
	app.run(host='0.0.0.0', port=port, debug=True)


