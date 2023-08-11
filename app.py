from flask import Flask,render_template,redirect,url_for

from views.home.home import home_blueprint
from views.portal.portal import portal_blueprint

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'your-secret-key'

app.register_blueprint(home_blueprint,url_prefix='/home')
app.register_blueprint(portal_blueprint,url_prefix='/portal')


@app.route('/')
def hello_world():  # put application's code here
    # return 'Hello World!'
    return redirect(url_for('home.home'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
