#this renders registration form 

from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from main.models import User

class RegisterForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired\
			("Username required")] )
	email = StringField("Email Address", validators=[DataRequired\
			("Email Address required"), Email\
			("Invalid Email address!")] )
	password = PasswordField("Password", validators=[DataRequired("Create Password"), Length(min=8)])
	confirm_password = PasswordField("Confirm Password", validators=[DataRequired("Password not confirmed"), EqualTo("password")])
	submit = SubmitField("Sign Up")
	
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('username already exists')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('email address already exists')

#this renders login form
class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired\
				("Invalid Username!")])
	password = PasswordField("Password", validators=[DataRequired\
				("Invalid Password!")])
	submit = SubmitField("Sign In")	
	
#this renders Compose form
class ComposeForm(FlaskForm):
	title = StringField("Title", validators=[DataRequired()])
	blog = TextAreaField("Blog", validators=[DataRequired()])
	submit = SubmitField("Post")
