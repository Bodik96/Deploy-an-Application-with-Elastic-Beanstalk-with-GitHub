from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from 3a5fda50 Elastic Beanstalk CI-CD verification-2026092006094310717"
