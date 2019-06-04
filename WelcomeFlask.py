#import package flask
import flask

# create object
app = flask.Flask(__name__)

# add url
@app.route('/', methods=['GET'])
def home():
    return "Welcome to Web API"
# define member


# run applications
app.run(host='0.0.0.0',port=5003)