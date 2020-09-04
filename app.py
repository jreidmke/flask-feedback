from flask import Flask, request, session, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Feedback
from forms import RegisterForm, LoginForm, FeedbackForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres4@localhost/feedback'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = "abc123"

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def redirect_register():
    return redirect('/register')

#Register User

@app.route('/register', methods=["GET", "POST"])
def register_user():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User.register(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        db.session.add(user)
        db.session.commit()
        # session['user_id'] = user.id
        flash(f"Welcome {user.first_name}!")
        return redirect('/register')

    return render_template('register.html', form=form)

#Login User

@app.route('/login', methods=["GET", "POST"])
def login_user():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if user:
            flash(f'Welcome back {user.first_name}!')
            session['user_id'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors=["Invalid Info"]
    return render_template('login.html', form=form)

@app.route('/users/<username>')
def show_secret(username):
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/login')
    user = User.query.get(username)
    feedback = user.feedback
    return render_template('user-detail.html', user=user, feedback=feedback)

#Logout User
@app.route('/logout', methods=["POST"])
def logout_user():
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/login')
    name = session['user_id']
    session.pop('user_id')
    flash(f'Goodbye {name}')
    return redirect('/')

#Delete user
@app.route('/users/<username>/delete', methods=["POST"])
def delete_user(username):
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/login')

    name = session['user_id']
    session.pop('user_id')
    user = User.query.get(username)
    db.session.delete(user)
    db.session.commit()
    flash(f'Goodbye {name}')
    return redirect('/')

#Make Post

@app.route('/users/<username>/feedback/add', methods=["GET", "POST"])
def add_feedback(username):
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/login')
    user = User.query.get(username)
    form = FeedbackForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        username = user.username
        fb = Feedback(title=title, content=content, username=username)
        db.session.add(fb)
        db.session.commit()
        flash(f'New post: {title} by {username}')
        return redirect(f'/users/{username}')
    return render_template('add-feedback.html', form = form)


#Edit Post
@app.route('/feedback/<feedback_id>/update', methods=["GET", "POST"])
def edit_feedback(feedback_id):
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/login')
    form = FeedbackForm()
    if form.validate_on_submit():
        fb = Feedback.query.get(feedback_id)
        fb.title = form.title.data
        fb.content = form.content.data
        fb.username = session['user_id']
        db.session.add(fb)
        db.session.commit()
        return redirect(f'/users/{fb.username}')
    return render_template('edit-feedback.html', form = form)





#Delete Post
@app.route('/feedback/<int:feedback_id>/delete', methods=["POST"])
def delete_feedback(feedback_id):
    if 'user_id' not in session:
        flash('Please login first')
        return redirect('/login')
    fb = Feedback.query.get(feedback_id)
    fb_title = fb.title
    username = fb.user.username
    db.session.delete(fb)
    db.session.commit()
    flash(f'{fb_title} Deleted')
    return redirect(f'/users/{username}')