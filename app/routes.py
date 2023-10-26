from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, DataForm
from app.models import User, Datapoint
import os

from app.helper import transform_datapoints
from app.plotandfit import plot_and_fit

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = DataForm()
    if form.validate_on_submit():
        data = Datapoint(user_id=current_user.id, weight=form.data.data)
        db.session.add(data)
        db.session.commit()
        flash('datapoint added!')
        x, y = transform_datapoints(datapoints=current_user.datapoints.all(), field="weight")
        plot_and_fit(x=x, y=y, savepath=r"C:\Users\Benja\Code\Python\Webside - Fitness\app\static\images\test.png")
    return render_template('index.html', title='Home', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data) 
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            return redirect(next_page)
    return render_template("login.html", title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


#login view for all
@app.route('/comparison', methods=['GET', 'POST'])
def comparison():
    full_filename = os.path.join(app.config['upload_folder'], 'test.png')
    return render_template('comparison.html', title='Comparison', test_image=full_filename)


#login view for yourself
@app.route('/home', methods=['GET', 'POST'])
def home():
    full_filename = os.path.join(app.config['upload_folder'], 'test.png')
    return render_template('home.html', title='MyHome', test_image=full_filename)