from flask import Flask, render_template,request,abort,jsonify,Blueprint,make_response
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy


from instance.config import app_config

db=SQLAlchemy()

mail = Mail()

def create_app(config_name):

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




	@app.route('/process', methods=['GET','POST'])
	def process():
		if request.method == "POST":
			print(request.form);
			Message = {"Message":"Welcome to chweyaassociates"}
		return render_template("contact.html")   

	return app
