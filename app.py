from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/user-info', methods = ['GET'])
def main():
    return 'user info working'

if __name__ == "__main__":
    app.run(port=4444, debug=True)
