from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/test")
def test():
    return "Testing the world!"

@application.route("/openshift")
def openshift():
    return "Hello OpenShift!"


if __name__ == "__main__":
    application.run()
