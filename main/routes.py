#routes file
from main import app
from flask import render_template, request, redirect, url_for, flash
from main import bcrypt, db
from main.forms import RegisterForm, LoginForm, ComposeForm
from main.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required, current_user


@app.route('/blogsforblogs')
@app.route('/blogsforblogs/register', methods = ['POST', 'GET'])
def register():
	form = RegisterForm() 
	if form.validate_on_submit() == False:
		return render_template("register.html", title="register", \
				form=form)
	else:
		encrypted_password = bcrypt.generate_password_hash(\
						form.password.data)
		user = User(username=form.username.data, email=form.email.data, password=encrypted_password)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))
	
@app.route('/blogsforblogs/login', methods = ['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			return redirect(url_for('home'))
		else:
			flash("invalid password or username!!!")
	return render_template("login.html", title="login", form=form)

@app.route('/blogsforblogs/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/blogsforblogs/home', methods=['GET', 'POST'])
def home():
	if current_user.is_authenticated:
		posts = Post.query.all()
		return render_template('home.html', title="home", posts=posts)
	else:
		return redirect(url_for('login'))
	
@app.route('/blogsforblogs/compose', methods=['GET', 'POST'])
@login_required
def compose():
	form = ComposeForm()
	if form.validate_on_submit() == False:
		return render_template('compose.html', title="compose", form=form)
	else:
		post = Post(title=form.title.data, blog=form.blog.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('home'))


@app.route('/blogsforblogs/post/<int:post_id>')
@login_required
def posts(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('posts.html', title="post", post=post)


	
