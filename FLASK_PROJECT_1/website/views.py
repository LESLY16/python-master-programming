from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__) #you can give any name insead of views in both places, 
                                     #second view is name of the blue print

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

