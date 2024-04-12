from flask import render_template, flash, request, redirect, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
import json
import stripe
from portfolio.forms import  RegistrationForm, LoginForm
from portfolio.models import User
import secrets
from portfolio import app, db, bcrypt
from sqlalchemy.exc import IntegrityError

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/companies')
def view_companies():
    # Render the companies template with the list of available companies
    return jsonify(companies)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return render_template('home_authenticated.html')
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        try:
            db.session.commit()
            flash('Account created', 'success')
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            flash('Username already exists. Please choose a different username.', 'danger')
            return redirect(url_for('register'))
    return render_template('register1.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template('home_authenticated.html')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return render_template('home_authenticated.html', username=user.username)
        else:
            flash('Login Unsuccessful, please check you email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'GET':
        # Your logic for handling GET requests goes here
        return render_template('edit_profile.html')
    elif request.method == 'POST':
        # Your logic for handling POST requests goes here
        return render_template('edit_profile.html')

@app.route('/send_parcel')
def send_parcel():
    # Implement the functionality for sending parcels here
    return render_template('track_parcel.html')


@app.route('/view_shipping_providers')
def view_shipping_providers():
    return render_template('view_shipping_providers.html')

@app.route('/update_profile')
def update():
    return render_template('home_authenticated.html')

@app.route('/about')
def about():
    # Implement the functionality for sending parcels here
    return render_template('about.html')


#if __name__ == "__main__":
#    app.secret_key = '361840c28c03f7721cae23e428f6dca5'
#    app.run(debug=True)
