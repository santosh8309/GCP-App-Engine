
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/login')
def login():
    """Return a friendly HTTP greeting."""
    return 'You are now seeing Login Page'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app.
    app.run()
# [END gae_flex_quickstart]
