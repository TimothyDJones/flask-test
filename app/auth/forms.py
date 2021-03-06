# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import AppUser

class RegistrationFrom(FlaskForm):
	"""
	Form for users to create new account
	"""
	email = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('User Name', validators=[DataRequired()])
	first_name = StringField('First Name', validators=[DataRequired()])
	last_name = StringField('Last Name', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password')])
	confirm_password = PasswordField('Confirm Password')
	submit = SubmitField('Register')

	def validate_email(self, field):
		if AppUser.query.filter_by(email=field.data).first():
			raise ValidationError('Email address is already used.')

	def validate_username(self, field):
		if AppUser.query.filter_by(username=field.data).first():
			raise ValidationError('User name is already used.')

class LoginForm(FlaskForm):
	"""
	Form for user log in
	"""
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')
