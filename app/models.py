# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class AppUser(UserMixin, db.Model):
	"""
	Create the application user table
	"""
	
	# Pluralize table name
	__tablename__ = 'appusers'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(60), index=True, unique=True)
	username = db.Column(db.String(60), index=True, unique=True)
	first_name = db.Column(db.String(60), index=False)
	last_name = db.Column(db.String(60), index=False)
	password_hash = db.Column(db.String(128))
	is_admin = db.Column(db.Boolean, default=False)

	@property
	def password(self):
		"""
		Prevent direct access to password attribute
		"""
		raise AttributeError("Password is not a readable attribute.")

	@password.setter
	def password(self, password):
		"""
		Set password to hashed value from input
		"""
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""
		Check input password against stored hashed password
		"""
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<AppUser: {}'.format(self.username)

@login_manager.user_loader
def load_user(user_id):
	return AppUser.query.get(int(user_id))

class Bookmark(db.Model):
	"""
	Create the bookmarks table
	"""

	__tablename__ = 'bookmarks'

	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(255), unique=True)
	title = db.Column(db.String(128))
	description = db.Column(db.String(255))
	users = db.relationship('AppUser', backref='bookmark', lazy='dynamic')

	def __repr__(self):
		return '<Bookmark: {}'.format(self.title)
