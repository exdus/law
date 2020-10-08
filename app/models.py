import os

from app import db
from flask_bcrypt import Bcrypt
import jwt
from datetime import datetime, timedelta


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)


    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = Bcrypt().generate_password_hash(
            password).decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_password_valid(self,password):
    	return Bcrypt().check_password_hash(self.password,password)

    def save(self):
    	db.session.add(self)
    	db.session.commit()

    def generate_token(self,user_id):
    	try:
    		payload = {
    		   "exp":datetime.utcnow() + timedelta(minutes=5),
    		   "iat":datetime.utcnow(),
    		   "sub":user_id
    		}
    		return jwt.encode(
    			payload,
    			app.config.get("SECRET"),
    			algorithm="HS256"
    			)
    		return 
    	except Exception as e:
    		return e


    @staticmethod
    def decode_token(token):
    	try:
    		payload=jwt.encode(token,app.config.get("SECRET"))
    		return payload["sub"]
    	except jwt.ExpiredSignatureError:
    		return "Signature expired, tafadhali log in again"
    	except jwt.InvalidTokenError:
    		return "Invalid token, tafadhali log in again"



class Supplier(db.Model):

	__tablename__ = 'suppliers'

	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(255),unique=True,nullable=False)
	date_created=db.Column(db.DateTime(),default=db.func.current_timestamp())
	date_modified=db.Column(db.DateTime(),default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
	products=db.relationship(
        'Products', order_by='Products.id', cascade="all, delete-orphan")

	#code=db.Column(db.Integer)

	def __init__(self,name,products):
		self.name=name
		self.products=products

	def save(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	@staticmethod
	def get_all():
		return Supplier.query.all()

	def __repr__(self,name):
		return "<Supplier: {}>".format(self.name)


class Products(db.Model):

	__tablename__ = "products"

	id=db.Column(db.Integer(),primary_key=True)
	name=db.Column(db.String(255),unique=True,nullable=False)
	supplier=db.relationship(
    'Supplier', order_by='Supplier.id', cascade="all, delete-orphan")

	def __init__(self,name,supplier,code):
		self.name=name
		self.supplier=supplier
		self.code=code

	def save():
		pass

	def delete(self):
		pass

	@staticmethod
	def get_all():
		pass


	def __repr__(self,name):
		return "Supplier {}".format(self.name)

class Vendor(db.Model):

	__tablename__ = "vendors"

	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(255),unique=True,nullable=False)
	date_created=db.Column(db.DateTime(),default=db.func.current_timestamp())
	date_modified=db.Column(db.DateTime(),default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
	address=db.Column(db.String(256))
	products=db.relationship(
    'Supplier', order_by='Supplier.id', cascade="all, delete-orphan")



	def __init__(self,name,supplier,code):
		self.name=name
		self.suppliers=supplier
		self.products=products

	def save():
		pass

	def delete(self):
		pass

	@staticmethod
	def get_all():
		pass


	def __repr__(self,name):
		return "Supplier {}".format(self.name)
