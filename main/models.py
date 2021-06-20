#database models
from main import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), unique=True,nullable=False)
	email = db.Column(db.String(180), unique=True, nullable=False)
	password = db.Column(db.String(180), nullable=False)
	
	posts = db.relationship('Post', backref='author', lazy=True)
	
	def __repr__(self):
		return 'User(%r, %r, %r)' %(self.username, self.email, self.password)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	blog = db.Column(db.String(1200), nullable=False)
	posted_date = db.Column(db.DateTime, nullable=False, \
				default=datetime.utcnow) 

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)	        

	def __repr__(self):
		return "Posts(%r, %r, %r, %r)" %(self.author, self.title, self.blog, \
				self.posted_date)      




