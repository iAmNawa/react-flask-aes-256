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
    from Cryptodome.Cipher import AES
    from hashlib import md5
    import base64

    user_string = request.args.get('user_string')
    password = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

    def unpad (padded):
        pad = ord(chr(padded[-1]))
        return padded[:-pad]

    def get_key_iv (password):
        m = md5()
        m.update(password.encode('utf-8'))
        key = m.hexdigest()

        m = md5()
        #use password and hexadecimal encoding to create initialization vector
        m.update((password + key).encode('utf-8'))
        iv = m.hexdigest()

        return [key,iv]

    def _decrypt(edata, password):
        edata = base64.urlsafe_b64decode(edata)
        key,iv = get_key_iv(password)

        aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv[:16].encode('utf-8'))
        return unpad(aes.decrypt(edata))

    plaintext = _decrypt(user_string, password)
    print(plaintext)

    return plaintext

if __name__ == "__main__":
    app.run(port=4444, debug=True)
