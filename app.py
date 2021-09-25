from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import jsonify
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/user-info', methods = ['GET'])
def main():
    key = '12345678'
    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
    user_string = request.args.get('user_string')
    result = decrypt(user_string)
    print(rersult)
    return result

if __name__ == "__main__":
    app.run(port=4444, debug=True)
