from flask import Flask, render_template,request,abort,jsonify,Blueprint,make_response
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config

db=SQLAlchemy()
mail = Mail()

def create_app(config_name):
	#from app.models import User, Supplier, Products, Vendor
	app=Flask(__name__,instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
	db.init_app(app)
	mail.init_app(app)

	@app.route("/")
	def landing_page():
		return "Welcome to Chweya And Associates"

	@app.route("/Home")
	def index():
		return render_template("index.html")


	@app.route("/About")
	def about():
		return render_template("about.html")

	@app.route("/Practice Areas")
	def practice_areas():
		return render_template("practice-area.html")

	@app.route("/Cases")
	def cases():
		return render_template("cases.html")

	@app.route("/Attorneys")
	def attorneys():
		return render_template("attorney.html")

	@app.route("/Blog")
	def blog():
		return render_template("blog.html")

	@app.route("/Contact")
	def contact():
		return render_template("contact.html")

	@app.route('/message', methods=['GET', 'POST'])
	def message():
	    """User can send e-mail via contact form"""

	    if request.method == 'POST':
	        """User sent an email request"""
	        msg = Message("Hello",
                  sender="keighb@live.com",
                  recipients=["scholarscarpak@gmail.com"])
	        msg.body = "You have received new feedback from {0} {1} <{2}>.\n\n {3}".format(
	            request.form['first-name'],
	            request.form['last-name'],
	            request.form['email'],
	            request.form['message'])
	        try:
	            mail.send(msg)
	            msg = "We will respond as soon as possible."
	            category = "success"
	        except Exception as err:
	            msg = str(err)
	            category = "danger"

	        resp = {'feedback': msg, 'category': category}
	        return make_response(jsonify(resp), 200)

	    elif request.method == 'GET':
	        """User is viewing the page"""
	        return render_template('contact.html')




	return app
