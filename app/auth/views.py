# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import AppUser

@auth.route('/register', methods=['GET', 'POST'])
def register():
	"""
	Handle requests to '/register' route.
	Add a user to DB via registration form.
	"""

	form = RegistrationForm()
	if form.validate_on_submit():
		appuser = AppUser(email=form.email.data,
					username=form.username.data,
					first_name=form.first_name.data,
					last_name=form.last_name.data,
					password=form.password.data)

		# Add to database
		db.session.add(appuser)
		db.session.commit()
		flash('Registration successful! You may now log in.')

		# Redirect to login page
		return redirect(url_for('auth.login'))

	# Otherwise, display the registration form.
	return render_template('auth/register.html', form=form, title="Register")

@auth.route('/login', methods=['GET', 'POST'])
def login():
	"""
	Handle requests to '/login' route.
	Log user into application via form.
	"""

	form = LoginForm()
	if form.validate_on_submit():
		# Determine if user already exists and validate password.
		appuser = AppUser.query.filter_by(email=form.email.data).first()
		if appuser is not None and appuser.verify_password(form.password.data):
			login_user(appuser)

			# Redirect to the dashboard page after login
			return redirect(url_for('home.dashboard'))

		# If invalid login credentials.
		else:
			flash('Invalid email or passord. Please try again.')

	# Otherwise, display login form.
	return render_template('auth/login.html', form=form, title="Log In")

@auth.route('/logout')
@login_required
def logout():
	"""
	Handle requests to '/logout' route.
	Log user out of system if logged in.
	"""

	logout_user()
	flash('You have successfully logged out.')

	# Redirect to login page
	return redirect(url_for('auth.login'))


