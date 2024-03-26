from flask import Flask, redirect, render_template, request, session, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_oauthlib.client import OAuth

from dotenv import load_dotenv
load_dotenv()

import os

# Configuring Flask-Login
login_manager = LoginManager()

app = Flask(__name__)

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    if user_id == "test_user":
        return User()
    return None

@app.route('/login')
def login():
    callback = url_for('authorized', _external=True) 
    return google.authorize(callback=callback)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hello'))

@app.route('/unauthorized')
def unauthorized():
    return "You must be logged in to access this page!"

@app.route('/hello')
@login_required
def hello():
    return render_template('hello.html')

oauth = OAuth(app)

google = oauth.remote_app(
    name = 'google',
    consumer_key = os.getenv('CLIENT_ID'),  
    consumer_secret = os.getenv('CLIENT_SECRET'),
    request_token_params = {
        'scope': 'email'
    },
    base_url = 'https://www.googleapis.com/userinfo/v2/me',
    request_token_url = None,
    access_token_method = 'POST',
    access_token_url = 'https://accounts.google.com/o/oauth2/token',
    authorize_url = 'https://accounts.google.com/o/oauth2/auth') 

@app.route('/authorized')
@google.authorized_handler
def authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    # Fetch user info
    session['google_token'] = (resp['access_token'], '')
    me = google.get('userinfo')
    return redirect(url_for('hello'))

# google_config = {
#     "client_id": os.getenv('CLIENT_ID'),
#     "client_secret": os.getenv('CLIENT_SECRET'),
#     "access_token_url": "https://accounts.google.com/o/oauth2/token",
#     "authorize_url": "https://accounts.google.com/o/oauth2/auth",
#     "api_base_url": "https://www.googleapis.com/userinfo/v2/",
# }

# google = oauth.register(
#     name='google',
#     server_metadata_url='https://accounts.google.com/.well-known/'
# )

if __name__ == '__main__':
    app.secret_key = 'thissecretistobeuntold'
    login_manager.init_app(app)
    app.run(host="127.0.0.1", port=5000)
