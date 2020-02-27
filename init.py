# Import
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

# Init
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/chains.db'
db=SQLAlchemy(app)

#Class DataModel
class Chain(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content=db.Column(db.String(200))
	hash_text=db.Column(db.String(200)) 

# Index route
# [GET]
@app.route('/')
def index():
	last= Chain.query.all()
	return render_template('index.html', last=last)

# Chain route
# [GET|POST]
@app.route('/chain', methods=['GET', 'POST'])
def chain():
	# POST
	if request.method == 'POST':
		chain= Chain(content=request.form['content'], hash_text=request.form['hash'])
		db.session.add(chain)
		db.session.commit()
		return redirect(url_for('index'))
		#return post(request.form['content'], request.form['hash'], request.form['algorithm'])

	# GET
	if request.method == 'GET':
		chains= Chain.query.order_by(desc(Chain.id)).limit(5)
		return render_template('index.html', chains= chains, last=last_chain)
		
	return list()

#Chain/last route for get last hash added
@app.route('/chain/last', methods=['GET'])
def last_chain():
	last= Chain.query.order_by(desc(Chain.id)).first()
	return render_template('index.html', last=last)

#api/v1/chain route for get a JSON view of data on database
@app.route('/api/v1/chain', methods=['GET'])
def list_json():
	chains= Chain.query.all()
	chain_json={}

	for chain in range(0,len(chains)):
		chain_json[chain+1]=chains[chain].hash_text
	
	if(chain_json):
		return jsonify(chain_json)
	else:
		return 'Database is empty... Please fill it'



# List function
# @return string
def list():
	return 'return list template'	## TODO

#pip3 install Flask-SQLAlchemy
#pip install -U Flask-SQLAlchemy
#pip3 install -U Flask-SQLAlchemy
#pip3 install sqlachemy
#pip install sqlachemy
#pip install Flask-SQLAlchemy
#settings.json {"python.pythonPath": "venv/bin/python3.7"}
#add in Import from flask_sqlalchemy import SQLAlchemy
#create a folder called database and then in venv : from flask_sqlalchemy import SQLAlchemy
# put .database or .databases
# add in Init app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/chains.db' and db=SQLAlchemy(app)

