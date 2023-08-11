import logging
from flask import Blueprint, render_template, request

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@home_blueprint.route('/home')
def home():

    return render_template('home.html')