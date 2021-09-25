import axios from 'axios'
import { Buffer } from 'buffer'

function InputComponent() {
  const sendData = () => {

    var aes256 = {},
        crypto = require('crypto'),
        algorithm = 'aes-256-cbc';

    aes256.encrypt = function (key, data) {
        var sha256 = crypto.createHash('sha256');
        sha256.update(key);

        var iv = crypto.randomBytes(16),
            plaintext = new Buffer(data),
            cipher = crypto.createCipheriv(algorithm, sha256.digest(), iv),
            ciphertext = cipher.update(plaintext);
        ciphertext = Buffer.concat([iv, ciphertext, cipher.final()]);

        return ciphertext.toString('base64');
  };
  let user_key = '12345678'
  let user_data = 'username'
  let encrypted_string = aes256.encrypt(user_key, user_data)
  console.log(encrypted_string)
    axios.get('http://localhost:4444/user-info', {
      params: { user_string: encrypted_string }
    })
      .then(res => {
        console.log(res)
      })
  }
  return (
    <div>
      <button onClick={sendData}>click me</button>
    </div>
  )
}

export default InputComponent
