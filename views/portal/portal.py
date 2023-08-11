import logging
from flask import Blueprint, render_template, request

portal_blueprint = Blueprint('portal', __name__, template_folder='templates', static_folder='static')

@portal_blueprint.route('/auth', methods=['GET', 'POST'])
def portal():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        # logger.info("portal test {} {}".format(username, password))

    return render_template('auth.html')