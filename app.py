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
    password = '00000000000000000000000000000000'
    iv = '0000000000000000';
    user_string = bytes(user_string, 'utf-8')
    print(user_string)
    def unpad (padded):
        pad = ord(chr(padded[-1]))
        return padded[:-pad]

    def _decrypt(edata, password):
        edata = base64.urlsafe_b64decode(edata)
        #key,iv = get_key_iv(password)

        aes = AES.new(password.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
        return unpad(aes.decrypt(edata))

    print(_decrypt(user_string, 'utf-8'), password)

    return 'hello'

if __name__ == "__main__":
    app.run(port=4444, debug=True)
