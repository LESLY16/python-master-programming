from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__) #you can give any name insead of auth in both places, 
                                     #second auth is name of the Blueprint
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods = ['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        firstname = request.form.get('firstName')
        password = request.form.get('password1')
        cpassword = request.form.get('password2')

        if len(email) < 4:
            flash("Email length must be atleast 4 characters long", category="error")
        elif len(firstname) < 2:
            flash("First Name must be atleast 2 characters long", category="error")
        elif password != cpassword:
            flash("Password and confirm password must match", category="error")
        elif len(password) < 7:
            flash("Length of password must be atleast 7 characters long", category="error")
        else:
            new_user = User(email=email, first_name=firstname, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)