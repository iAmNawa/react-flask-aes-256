from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify
import base64
import hashlib
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome import Random
from Cryptodome.Cipher import AES


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/user-info', methods = ['GET'])
def main():

    user_string = request.args.get('user_string')
    key = b'1234567890123456'
    enc = base64.b64decode(user_string)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    username = cipher.decrypt(user_string, 'utf-8')
    print(len(username))
    user_string = request.args.get('user_string')

    return result

if __name__ == "__main__":
    app.run(port=4444, debug=True)
